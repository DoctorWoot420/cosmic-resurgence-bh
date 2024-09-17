The default maphack configuration for the Resurgence Diablo II mod.  This repo is consumed directly by the filter configurator immediately on push.

As the name implies, this version is produced by Cosmic.  It's targeted for use with Rusty's branch of SlashDiablo Maphack 1.9.10.  Based on the original resurgence bh configuration by Planqi.



Overview of notify-dead and progressively filtering items
* Many times you want an item to ping early on, but get completely filteted out eventually.  This is possible with multiple lines, but each line must work with eachother.
* When an error occurs, you'll see [blocked] in the item names.  This means a line matched the item somewhere in the file, and then it was filtered out by another line after.
* notify-dead means "show this item, but not on the map"

You have 3 choices for progressively filtering items:
* Tier only: good for high tier items that never filter
* Tier + notify-dead: use this combo when an item should ping at first, then drop to map-only after a tier, but never get filtered
* Tier + notify-dead + filter line (blank item name output): use this combo to have something progress from a pingable item, to map-only, to eventually getting filtered out.

Unless something should be visibile at filter 3, it must have a notify-dead and/or a filter line, if it also has a tier line somewhere.
You don't have to define a filter line for every tiered line because there are catch-all filters on bottom.  For any rare/craft/alch lines that you want to filter, you only need to specify the FILTLVL<X criteria on the target lines.  Just make that your criteria is the filter level below what that item would get filtered at below.  For example elite rare items dont get filtered until FILT 3 at bottom, so a rare line to highlight them would be like (ulb) (RARE) (FILTLVL<3) (otherCriteriaHere), then you can count on it matching the generic filter line once it hits filt 3.


Filter blocks
* Filter blocks work by combining BH.cfg with zero, or many files within the filter-blocks folder
* Duplicate lines freely between blocks, they are removed when the config is generated
* New filter blocks need to be manually included in the launcher configuration

