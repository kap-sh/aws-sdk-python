"""Generated from Smithy shape ``com.amazonaws.mediaconvert#BurninDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min0_max10
    import capo_mediaconvert.types.__integer_min0_max96
    import capo_mediaconvert.types.__integer_min0_max255
    import capo_mediaconvert.types.__integer_min0_max2147483647
    import capo_mediaconvert.types.__integer_min96_max600
    import capo_mediaconvert.types.__integer_min_negative2147483648_max2147483647
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.__string_min6_max8_pattern09a_faf609a_faf2
    import capo_mediaconvert.types.__string_pattern_s3_ttf_https_ttf
    import capo_mediaconvert.types.burn_in_subtitle_style_passthrough
    import capo_mediaconvert.types.burnin_subtitle_alignment
    import capo_mediaconvert.types.burnin_subtitle_apply_font_color
    import capo_mediaconvert.types.burnin_subtitle_background_color
    import capo_mediaconvert.types.burnin_subtitle_fallback_font
    import capo_mediaconvert.types.burnin_subtitle_font_color
    import capo_mediaconvert.types.burnin_subtitle_outline_color
    import capo_mediaconvert.types.burnin_subtitle_shadow_color
    import capo_mediaconvert.types.burnin_subtitle_teletext_spacing
    import capo_mediaconvert.types.font_script
    import capo_mediaconvert.types.remove_ruby_reserve_attributes


class BurninDestinationSettings(TypedDict, closed=True):
    alignment: NotRequired[
        "capo_mediaconvert.types.burnin_subtitle_alignment.BurninSubtitleAlignment"
    ]
    """Specify the alignment of your captions. If no explicit x_position is provided, setting alignment to centered will placethe captions at the bottom center of the output. Similarly, setting a left alignment willalign captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates."""
    apply_font_color: NotRequired[
        "capo_mediaconvert.types.burnin_subtitle_apply_font_color.BurninSubtitleApplyFontColor"
    ]
    """Ignore this setting unless Style passthrough is set to Enabled and Font color set to Black, Yellow, Red, Green, Blue, or Hex. Use Apply font color for additional font color controls. When you choose White text only, or leave blank, your font color setting only applies to white text in your input captions. For example, if your font color setting is Yellow, and your input captions have red and white text, your output captions will have red and yellow text. When you choose ALL_TEXT, your font color setting applies to all of your output captions text."""
    background_color: NotRequired[
        "capo_mediaconvert.types.burnin_subtitle_background_color.BurninSubtitleBackgroundColor"
    ]
    """Specify the color of the rectangle behind the captions. Leave background color blank and set Style passthrough to enabled to use the background color data from your input captions, if present."""
    background_opacity: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max255.__integerMin0Max255"
    ]
    """Specify the opacity of the background rectangle. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to enabled, leave blank to pass through the background style information in your input captions to your output captions. If Style passthrough is set to disabled, leave blank to use a value of 0 and remove all backgrounds from your output captions."""
    fallback_font: NotRequired[
        "capo_mediaconvert.types.burnin_subtitle_fallback_font.BurninSubtitleFallbackFont"
    ]
    """Specify the font that you want the service to use for your burn in captions when your input captions specify a font that MediaConvert doesn't support. When you set Fallback font to best match, or leave blank, MediaConvert uses a supported font that most closely matches the font that your input captions specify. When there are multiple unsupported fonts in your input captions, MediaConvert matches each font with the supported font that matches best. When you explicitly choose a replacement font, MediaConvert uses that font to replace all unsupported fonts from your input."""
    font_color: NotRequired[
        "capo_mediaconvert.types.burnin_subtitle_font_color.BurninSubtitleFontColor"
    ]
    """Specify the color of the burned-in captions text. Leave Font color blank and set Style passthrough to enabled to use the font color data from your input captions, if present."""
    font_file_bold: NotRequired[
        "capo_mediaconvert.types.__string_pattern_s3_ttf_https_ttf.__stringPatternS3TtfHttpsTtf"
    ]
    """Specify a bold TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, an italic, and a bold italic font file."""
    font_file_bold_italic: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Specify a bold italic TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, a bold, and an italic font file."""
    font_file_italic: NotRequired[
        "capo_mediaconvert.types.__string_pattern_s3_ttf_https_ttf.__stringPatternS3TtfHttpsTtf"
    ]
    """Specify an italic TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, a bold, and a bold italic font file."""
    font_file_regular: NotRequired[
        "capo_mediaconvert.types.__string_pattern_s3_ttf_https_ttf.__stringPatternS3TtfHttpsTtf"
    ]
    """Specify a regular TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a bold, an italic, and a bold italic font file."""
    font_opacity: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max255.__integerMin0Max255"
    ]
    """Specify the opacity of the burned-in captions. 255 is opaque; 0 is transparent."""
    font_resolution: NotRequired[
        "capo_mediaconvert.types.__integer_min96_max600.__integerMin96Max600"
    ]
    """Specify the Font resolution in DPI (dots per inch)."""
    font_script: NotRequired["capo_mediaconvert.types.font_script.FontScript"]
    """Set Font script to Automatically determined, or leave blank, to automatically determine the font script in your input captions. Otherwise, set to Simplified Chinese (HANS) or Traditional Chinese (HANT) if your input font script uses Simplified or Traditional Chinese."""
    font_size: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max96.__integerMin0Max96"
    ]
    """Specify the Font size in pixels. Must be a positive integer. Set to 0, or leave blank, for automatic font size."""
    hex_font_color: NotRequired[
        "capo_mediaconvert.types.__string_min6_max8_pattern09a_faf609a_faf2.__stringMin6Max8Pattern09aFAF609aFAF2"
    ]
    """Ignore this setting unless your Font color is set to Hex. Enter either six or eight hexidecimal digits, representing red, green, and blue, with two optional extra digits for alpha. For example a value of 1122AABB is a red value of 0x11, a green value of 0x22, a blue value of 0xAA, and an alpha value of 0xBB."""
    outline_color: NotRequired[
        "capo_mediaconvert.types.burnin_subtitle_outline_color.BurninSubtitleOutlineColor"
    ]
    """Specify font outline color. Leave Outline color blank and set Style passthrough to enabled to use the font outline color data from your input captions, if present."""
    outline_size: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max10.__integerMin0Max10"
    ]
    """Specify the Outline size of the caption text, in pixels. Leave Outline size blank and set Style passthrough to enabled to use the outline size data from your input captions, if present."""
    remove_ruby_reserve_attributes: NotRequired[
        "capo_mediaconvert.types.remove_ruby_reserve_attributes.RemoveRubyReserveAttributes"
    ]
    """Optionally remove any tts:rubyReserve attributes present in your input, that do not have a tts:ruby attribute in the same element, from your output. Use if your vertical Japanese output captions have alignment issues. To remove ruby reserve attributes when present: Choose Enabled. To not remove any ruby reserve attributes: Keep the default value, Disabled."""
    shadow_color: NotRequired[
        "capo_mediaconvert.types.burnin_subtitle_shadow_color.BurninSubtitleShadowColor"
    ]
    """Specify the color of the shadow cast by the captions. Leave Shadow color blank and set Style passthrough to enabled to use the shadow color data from your input captions, if present."""
    shadow_opacity: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max255.__integerMin0Max255"
    ]
    """Specify the opacity of the shadow. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to Enabled, leave Shadow opacity blank to pass through the shadow style information in your input captions to your output captions. If Style passthrough is set to disabled, leave blank to use a value of 0 and remove all shadows from your output captions."""
    shadow_x_offset: NotRequired[
        "capo_mediaconvert.types.__integer_min_negative2147483648_max2147483647.__integerMinNegative2147483648Max2147483647"
    ]
    """Specify the horizontal offset of the shadow, relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left."""
    shadow_y_offset: NotRequired[
        "capo_mediaconvert.types.__integer_min_negative2147483648_max2147483647.__integerMinNegative2147483648Max2147483647"
    ]
    """Specify the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. Leave Shadow y-offset blank and set Style passthrough to enabled to use the shadow y-offset data from your input captions, if present."""
    style_passthrough: NotRequired[
        "capo_mediaconvert.types.burn_in_subtitle_style_passthrough.BurnInSubtitleStylePassthrough"
    ]
    """To use the available style, color, and position information from your input captions: Set Style passthrough to Enabled. Note that MediaConvert uses default settings for any missing style or position information in your input captions To ignore the style and position information from your input captions and use default settings: Leave blank or keep the default value, Disabled. Default settings include white text with black outlining, bottom-center positioning, and automatic sizing. Whether you set Style passthrough to enabled or not, you can also choose to manually override any of the individual style and position settings. You can also override any fonts by manually specifying custom font files."""
    teletext_spacing: NotRequired[
        "capo_mediaconvert.types.burnin_subtitle_teletext_spacing.BurninSubtitleTeletextSpacing"
    ]
    """Specify whether the text spacing in your captions is set by the captions grid, or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read for closed captions."""
    x_position: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the horizontal position of the captions, relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit x_position is provided, the horizontal caption position will be determined by the alignment parameter."""
    y_position: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the vertical position of the captions, relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit y_position is provided, the caption will be positioned towards the bottom of the output."""


# --- restJson1 ser/de ---
def serialize_json(value: BurninDestinationSettings) -> dict:
    out: dict = {}
    if "alignment" in value:
        import capo_mediaconvert.types.burnin_subtitle_alignment

        out["alignment"] = (
            capo_mediaconvert.types.burnin_subtitle_alignment.serialize_json(
                value["alignment"]
            )
        )
    if "apply_font_color" in value:
        import capo_mediaconvert.types.burnin_subtitle_apply_font_color

        out["applyFontColor"] = (
            capo_mediaconvert.types.burnin_subtitle_apply_font_color.serialize_json(
                value["apply_font_color"]
            )
        )
    if "background_color" in value:
        import capo_mediaconvert.types.burnin_subtitle_background_color

        out["backgroundColor"] = (
            capo_mediaconvert.types.burnin_subtitle_background_color.serialize_json(
                value["background_color"]
            )
        )
    if "background_opacity" in value:
        out["backgroundOpacity"] = value["background_opacity"]
    if "fallback_font" in value:
        import capo_mediaconvert.types.burnin_subtitle_fallback_font

        out["fallbackFont"] = (
            capo_mediaconvert.types.burnin_subtitle_fallback_font.serialize_json(
                value["fallback_font"]
            )
        )
    if "font_color" in value:
        import capo_mediaconvert.types.burnin_subtitle_font_color

        out["fontColor"] = (
            capo_mediaconvert.types.burnin_subtitle_font_color.serialize_json(
                value["font_color"]
            )
        )
    if "font_file_bold" in value:
        out["fontFileBold"] = value["font_file_bold"]
    if "font_file_bold_italic" in value:
        out["fontFileBoldItalic"] = value["font_file_bold_italic"]
    if "font_file_italic" in value:
        out["fontFileItalic"] = value["font_file_italic"]
    if "font_file_regular" in value:
        out["fontFileRegular"] = value["font_file_regular"]
    if "font_opacity" in value:
        out["fontOpacity"] = value["font_opacity"]
    if "font_resolution" in value:
        out["fontResolution"] = value["font_resolution"]
    if "font_script" in value:
        import capo_mediaconvert.types.font_script

        out["fontScript"] = capo_mediaconvert.types.font_script.serialize_json(
            value["font_script"]
        )
    if "font_size" in value:
        out["fontSize"] = value["font_size"]
    if "hex_font_color" in value:
        out["hexFontColor"] = value["hex_font_color"]
    if "outline_color" in value:
        import capo_mediaconvert.types.burnin_subtitle_outline_color

        out["outlineColor"] = (
            capo_mediaconvert.types.burnin_subtitle_outline_color.serialize_json(
                value["outline_color"]
            )
        )
    if "outline_size" in value:
        out["outlineSize"] = value["outline_size"]
    if "remove_ruby_reserve_attributes" in value:
        import capo_mediaconvert.types.remove_ruby_reserve_attributes

        out["removeRubyReserveAttributes"] = (
            capo_mediaconvert.types.remove_ruby_reserve_attributes.serialize_json(
                value["remove_ruby_reserve_attributes"]
            )
        )
    if "shadow_color" in value:
        import capo_mediaconvert.types.burnin_subtitle_shadow_color

        out["shadowColor"] = (
            capo_mediaconvert.types.burnin_subtitle_shadow_color.serialize_json(
                value["shadow_color"]
            )
        )
    if "shadow_opacity" in value:
        out["shadowOpacity"] = value["shadow_opacity"]
    if "shadow_x_offset" in value:
        out["shadowXOffset"] = value["shadow_x_offset"]
    if "shadow_y_offset" in value:
        out["shadowYOffset"] = value["shadow_y_offset"]
    if "style_passthrough" in value:
        import capo_mediaconvert.types.burn_in_subtitle_style_passthrough

        out["stylePassthrough"] = (
            capo_mediaconvert.types.burn_in_subtitle_style_passthrough.serialize_json(
                value["style_passthrough"]
            )
        )
    if "teletext_spacing" in value:
        import capo_mediaconvert.types.burnin_subtitle_teletext_spacing

        out["teletextSpacing"] = (
            capo_mediaconvert.types.burnin_subtitle_teletext_spacing.serialize_json(
                value["teletext_spacing"]
            )
        )
    if "x_position" in value:
        out["xPosition"] = value["x_position"]
    if "y_position" in value:
        out["yPosition"] = value["y_position"]
    return out


def deserialize_json(data: dict) -> BurninDestinationSettings:
    out: BurninDestinationSettings = {}  # type: ignore[typeddict-item]
    if "alignment" in data:
        import capo_mediaconvert.types.burnin_subtitle_alignment

        out["alignment"] = (
            capo_mediaconvert.types.burnin_subtitle_alignment.deserialize_json(
                data["alignment"]
            )
        )
    if "applyFontColor" in data:
        import capo_mediaconvert.types.burnin_subtitle_apply_font_color

        out["apply_font_color"] = (
            capo_mediaconvert.types.burnin_subtitle_apply_font_color.deserialize_json(
                data["applyFontColor"]
            )
        )
    if "backgroundColor" in data:
        import capo_mediaconvert.types.burnin_subtitle_background_color

        out["background_color"] = (
            capo_mediaconvert.types.burnin_subtitle_background_color.deserialize_json(
                data["backgroundColor"]
            )
        )
    if "backgroundOpacity" in data:
        out["background_opacity"] = data["backgroundOpacity"]
    if "fallbackFont" in data:
        import capo_mediaconvert.types.burnin_subtitle_fallback_font

        out["fallback_font"] = (
            capo_mediaconvert.types.burnin_subtitle_fallback_font.deserialize_json(
                data["fallbackFont"]
            )
        )
    if "fontColor" in data:
        import capo_mediaconvert.types.burnin_subtitle_font_color

        out["font_color"] = (
            capo_mediaconvert.types.burnin_subtitle_font_color.deserialize_json(
                data["fontColor"]
            )
        )
    if "fontFileBold" in data:
        out["font_file_bold"] = data["fontFileBold"]
    if "fontFileBoldItalic" in data:
        out["font_file_bold_italic"] = data["fontFileBoldItalic"]
    if "fontFileItalic" in data:
        out["font_file_italic"] = data["fontFileItalic"]
    if "fontFileRegular" in data:
        out["font_file_regular"] = data["fontFileRegular"]
    if "fontOpacity" in data:
        out["font_opacity"] = data["fontOpacity"]
    if "fontResolution" in data:
        out["font_resolution"] = data["fontResolution"]
    if "fontScript" in data:
        import capo_mediaconvert.types.font_script

        out["font_script"] = capo_mediaconvert.types.font_script.deserialize_json(
            data["fontScript"]
        )
    if "fontSize" in data:
        out["font_size"] = data["fontSize"]
    if "hexFontColor" in data:
        out["hex_font_color"] = data["hexFontColor"]
    if "outlineColor" in data:
        import capo_mediaconvert.types.burnin_subtitle_outline_color

        out["outline_color"] = (
            capo_mediaconvert.types.burnin_subtitle_outline_color.deserialize_json(
                data["outlineColor"]
            )
        )
    if "outlineSize" in data:
        out["outline_size"] = data["outlineSize"]
    if "removeRubyReserveAttributes" in data:
        import capo_mediaconvert.types.remove_ruby_reserve_attributes

        out["remove_ruby_reserve_attributes"] = (
            capo_mediaconvert.types.remove_ruby_reserve_attributes.deserialize_json(
                data["removeRubyReserveAttributes"]
            )
        )
    if "shadowColor" in data:
        import capo_mediaconvert.types.burnin_subtitle_shadow_color

        out["shadow_color"] = (
            capo_mediaconvert.types.burnin_subtitle_shadow_color.deserialize_json(
                data["shadowColor"]
            )
        )
    if "shadowOpacity" in data:
        out["shadow_opacity"] = data["shadowOpacity"]
    if "shadowXOffset" in data:
        out["shadow_x_offset"] = data["shadowXOffset"]
    if "shadowYOffset" in data:
        out["shadow_y_offset"] = data["shadowYOffset"]
    if "stylePassthrough" in data:
        import capo_mediaconvert.types.burn_in_subtitle_style_passthrough

        out["style_passthrough"] = (
            capo_mediaconvert.types.burn_in_subtitle_style_passthrough.deserialize_json(
                data["stylePassthrough"]
            )
        )
    if "teletextSpacing" in data:
        import capo_mediaconvert.types.burnin_subtitle_teletext_spacing

        out["teletext_spacing"] = (
            capo_mediaconvert.types.burnin_subtitle_teletext_spacing.deserialize_json(
                data["teletextSpacing"]
            )
        )
    if "xPosition" in data:
        out["x_position"] = data["xPosition"]
    if "yPosition" in data:
        out["y_position"] = data["yPosition"]
    return out
