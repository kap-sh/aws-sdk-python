"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__double_min0
    import aws_sdk_mediaconvert.types.__integer_min0_max7
    import aws_sdk_mediaconvert.types.__integer_min0_max30
    import aws_sdk_mediaconvert.types.__integer_min0_max100
    import aws_sdk_mediaconvert.types.__integer_min0_max128
    import aws_sdk_mediaconvert.types.__integer_min0_max1152000000
    import aws_sdk_mediaconvert.types.__integer_min0_max2147483647
    import aws_sdk_mediaconvert.types.__integer_min1_max6
    import aws_sdk_mediaconvert.types.__integer_min1_max32
    import aws_sdk_mediaconvert.types.__integer_min1_max2147483647
    import aws_sdk_mediaconvert.types.__integer_min1000_max1152000000
    import aws_sdk_mediaconvert.types.__list_of_frame_metric_type
    import aws_sdk_mediaconvert.types.bandwidth_reduction_filter
    import aws_sdk_mediaconvert.types.h264_adaptive_quantization
    import aws_sdk_mediaconvert.types.h264_codec_level
    import aws_sdk_mediaconvert.types.h264_codec_profile
    import aws_sdk_mediaconvert.types.h264_dynamic_sub_gop
    import aws_sdk_mediaconvert.types.h264_end_of_stream_markers
    import aws_sdk_mediaconvert.types.h264_entropy_encoding
    import aws_sdk_mediaconvert.types.h264_field_encoding
    import aws_sdk_mediaconvert.types.h264_flicker_adaptive_quantization
    import aws_sdk_mediaconvert.types.h264_framerate_control
    import aws_sdk_mediaconvert.types.h264_framerate_conversion_algorithm
    import aws_sdk_mediaconvert.types.h264_gop_b_reference
    import aws_sdk_mediaconvert.types.h264_gop_size_units
    import aws_sdk_mediaconvert.types.h264_interlace_mode
    import aws_sdk_mediaconvert.types.h264_par_control
    import aws_sdk_mediaconvert.types.h264_quality_tuning_level
    import aws_sdk_mediaconvert.types.h264_qvbr_settings
    import aws_sdk_mediaconvert.types.h264_rate_control_mode
    import aws_sdk_mediaconvert.types.h264_repeat_pps
    import aws_sdk_mediaconvert.types.h264_saliency_aware_encoding
    import aws_sdk_mediaconvert.types.h264_scan_type_conversion_mode
    import aws_sdk_mediaconvert.types.h264_scene_change_detect
    import aws_sdk_mediaconvert.types.h264_slow_pal
    import aws_sdk_mediaconvert.types.h264_spatial_adaptive_quantization
    import aws_sdk_mediaconvert.types.h264_syntax
    import aws_sdk_mediaconvert.types.h264_telecine
    import aws_sdk_mediaconvert.types.h264_temporal_adaptive_quantization
    import aws_sdk_mediaconvert.types.h264_unregistered_sei_timecode
    import aws_sdk_mediaconvert.types.h264_write_mp4_packaging_type


class H264Settings(TypedDict, closed=True):
    adaptive_quantization: NotRequired[
        "aws_sdk_mediaconvert.types.h264_adaptive_quantization.H264AdaptiveQuantization"
    ]
    """Keep the default value, Auto, for this setting to have MediaConvert automatically apply the best types of quantization for your video content. When you want to apply your quantization settings manually, you must set H264AdaptiveQuantization to a value other than Auto. Use this setting to specify the strength of any adaptive quantization filters that you enable. If you don't want MediaConvert to do any adaptive quantization in this transcode, set Adaptive quantization to Off. Related settings: The value that you choose here applies to the following settings: H264FlickerAdaptiveQuantization, H264SpatialAdaptiveQuantization, and H264TemporalAdaptiveQuantization."""
    bandwidth_reduction_filter: NotRequired[
        "aws_sdk_mediaconvert.types.bandwidth_reduction_filter.BandwidthReductionFilter"
    ]
    """The Bandwidth reduction filter increases the video quality of your output relative to its bitrate. Use to lower the bitrate of your constant quality QVBR output, with little or no perceptual decrease in quality. Or, use to increase the video quality of outputs with other rate control modes relative to the bitrate that you specify. Bandwidth reduction increases further when your input is low quality or noisy. Outputs that use this feature incur pro-tier pricing. When you include Bandwidth reduction filter, you cannot include the Noise reducer preprocessor."""
    bitrate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1000_max1152000000.__integerMin1000Max1152000000"
    ]
    """Specify the average bitrate in bits per second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000."""
    codec_level: NotRequired[
        "aws_sdk_mediaconvert.types.h264_codec_level.H264CodecLevel"
    ]
    """Specify an H.264 level that is consistent with your output video settings. If you aren't sure what level to specify, choose Auto."""
    codec_profile: NotRequired[
        "aws_sdk_mediaconvert.types.h264_codec_profile.H264CodecProfile"
    ]
    """H.264 Profile. High 4:2:2 and 10-bit profiles are only available with the AVC-I License."""
    dynamic_sub_gop: NotRequired[
        "aws_sdk_mediaconvert.types.h264_dynamic_sub_gop.H264DynamicSubGop"
    ]
    """Specify whether to allow the number of B-frames in your output GOP structure to vary or not depending on your input video content. To improve the subjective video quality of your output that has high-motion content: Leave blank or keep the default value Adaptive. MediaConvert will use fewer B-frames for high-motion video content than low-motion content. The maximum number of B- frames is limited by the value that you choose for B-frames between reference frames. To use the same number B-frames for all types of content: Choose Static."""
    end_of_stream_markers: NotRequired[
        "aws_sdk_mediaconvert.types.h264_end_of_stream_markers.H264EndOfStreamMarkers"
    ]
    """Optionally include or suppress markers at the end of your output that signal the end of the video stream. To include end of stream markers: Leave blank or keep the default value, Include. To not include end of stream markers: Choose Suppress. This is useful when your output will be inserted into another stream."""
    entropy_encoding: NotRequired[
        "aws_sdk_mediaconvert.types.h264_entropy_encoding.H264EntropyEncoding"
    ]
    """Entropy encoding mode. Use CABAC (must be in Main or High profile) or CAVLC."""
    field_encoding: NotRequired[
        "aws_sdk_mediaconvert.types.h264_field_encoding.H264FieldEncoding"
    ]
    """The video encoding method for your MPEG-4 AVC output. Keep the default value, PAFF, to have MediaConvert use PAFF encoding for interlaced outputs. Choose Force field to disable PAFF encoding and create separate interlaced fields. Choose MBAFF to disable PAFF and have MediaConvert use MBAFF encoding for interlaced outputs."""
    flicker_adaptive_quantization: NotRequired[
        "aws_sdk_mediaconvert.types.h264_flicker_adaptive_quantization.H264FlickerAdaptiveQuantization"
    ]
    """Only use this setting when you change the default value, AUTO, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264FlickerAdaptiveQuantization is Disabled. Change this value to Enabled to reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. To manually enable or disable H264FlickerAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO."""
    framerate_control: NotRequired[
        "aws_sdk_mediaconvert.types.h264_framerate_control.H264FramerateControl"
    ]
    """If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction."""
    framerate_conversion_algorithm: NotRequired[
        "aws_sdk_mediaconvert.types.h264_framerate_conversion_algorithm.H264FramerateConversionAlgorithm"
    ]
    """Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates."""
    framerate_denominator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976."""
    framerate_numerator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976."""
    gop_b_reference: NotRequired[
        "aws_sdk_mediaconvert.types.h264_gop_b_reference.H264GopBReference"
    ]
    """Specify whether to allow B-frames to be referenced by other frame types. To use reference B-frames when your GOP structure has 1 or more B-frames: Leave blank or keep the default value Enabled. We recommend that you choose Enabled to help improve the video quality of your output relative to its bitrate. To not use reference B-frames: Choose Disabled."""
    gop_closed_cadence: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the relative frequency of open to closed GOPs in this output. For example, if you want to allow four open GOPs and then require a closed GOP, set this value to 5. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. In the console, do this by keeping the default empty value. If you do explicitly specify a value, for segmented outputs, don't set this value to 0."""
    gop_size: NotRequired["aws_sdk_mediaconvert.types.__double_min0.__doubleMin0"]
    """Use this setting only when you set GOP mode control to Specified, frames or Specified, seconds. Specify the GOP length using a whole number of frames or a decimal value of seconds. MediaConvert will interpret this value as frames or seconds depending on the value you choose for GOP mode control. If you want to allow MediaConvert to automatically determine GOP size, leave GOP size blank and set GOP mode control to Auto. If your output group specifies HLS, DASH, or CMAF, leave GOP size blank and set GOP mode control to Auto in each output in your output group."""
    gop_size_units: NotRequired[
        "aws_sdk_mediaconvert.types.h264_gop_size_units.H264GopSizeUnits"
    ]
    """Specify how the transcoder determines GOP size for this output. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, choose Auto and and leave GOP size blank. By default, if you don't specify GOP mode control, MediaConvert will use automatic behavior. If your output group specifies HLS, DASH, or CMAF, set GOP mode control to Auto and leave GOP size blank in each output in your output group. To explicitly specify the GOP length, choose Specified, frames or Specified, seconds and then provide the GOP length in the related setting GOP size."""
    hrd_buffer_final_fill_percentage: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max100.__integerMin0Max100"
    ]
    """If your downstream systems have strict buffer requirements: Specify the minimum percentage of the HRD buffer that's available at the end of each encoded video segment. For the best video quality: Set to 0 or leave blank to automatically determine the final buffer fill percentage."""
    hrd_buffer_initial_fill_percentage: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max100.__integerMin0Max100"
    ]
    """Percentage of the buffer that should initially be filled (HRD buffer model)."""
    hrd_buffer_size: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max1152000000.__integerMin0Max1152000000"
    ]
    """Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000."""
    interlace_mode: NotRequired[
        "aws_sdk_mediaconvert.types.h264_interlace_mode.H264InterlaceMode"
    ]
    """Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose."""
    max_bitrate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1000_max1152000000.__integerMin1000Max1152000000"
    ]
    """Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR."""
    min_i_interval: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max30.__integerMin0Max30"
    ]
    """Specify the minimum number of frames allowed between two IDR-frames in your output. This includes frames created at the start of a GOP or a scene change. Use Min I-Interval to improve video compression by varying GOP size when two IDR-frames would be created near each other. For example, if a regular cadence-driven IDR-frame would fall within 5 frames of a scene-change IDR-frame, and you set Min I-interval to 5, then the encoder would only write an IDR-frame for the scene-change. In this way, one GOP is shortened or extended. If a cadence-driven IDR-frame would be further than 5 frames from a scene-change IDR-frame, then the encoder leaves all IDR-frames in place. To use an automatically determined interval: We recommend that you keep this value blank. This allows for MediaConvert to use an optimal setting according to the characteristics of your input video, and results in better video compression. To manually specify an interval: Enter a value from 1 to 30. Use when your downstream systems have specific GOP size requirements. To disable GOP size variance: Enter 0. MediaConvert will only create IDR-frames at the start of your output's cadence-driven GOP. Use when your downstream systems require a regular GOP size."""
    number_b_frames_between_reference_frames: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max7.__integerMin0Max7"
    ]
    """Specify the number of B-frames between reference frames in this output. For the best video quality: Leave blank. MediaConvert automatically determines the number of B-frames to use based on the characteristics of your input video. To manually specify the number of B-frames between reference frames: Enter an integer from 0 to 7."""
    number_reference_frames: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max6.__integerMin1Max6"
    ]
    """Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding."""
    par_control: NotRequired[
        "aws_sdk_mediaconvert.types.h264_par_control.H264ParControl"
    ]
    """Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings."""
    par_denominator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33."""
    par_numerator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40."""
    per_frame_metrics: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_frame_metric_type.__listOfFrameMetricType"
    ]
    """Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: * PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. * SHOT_CHANGE: Shot Changes"""
    quality_tuning_level: NotRequired[
        "aws_sdk_mediaconvert.types.h264_quality_tuning_level.H264QualityTuningLevel"
    ]
    """The Quality tuning level you choose represents a trade-off between the encoding speed of your job and the output video quality. For the fastest encoding speed at the cost of video quality: Choose Single pass. For a good balance between encoding speed and video quality: Leave blank or keep the default value Single pass HQ. For the best video quality, at the cost of encoding speed: Choose Multi pass HQ. MediaConvert performs an analysis pass on your input followed by an encoding pass. Outputs that use this feature incur pro-tier pricing."""
    qvbr_settings: NotRequired[
        "aws_sdk_mediaconvert.types.h264_qvbr_settings.H264QvbrSettings"
    ]
    """Settings for quality-defined variable bitrate encoding with the H.265 codec. Use these settings only when you set QVBR for Rate control mode."""
    rate_control_mode: NotRequired[
        "aws_sdk_mediaconvert.types.h264_rate_control_mode.H264RateControlMode"
    ]
    """Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR)."""
    repeat_pps: NotRequired["aws_sdk_mediaconvert.types.h264_repeat_pps.H264RepeatPps"]
    """Places a PPS header on each encoded picture, even if repeated."""
    saliency_aware_encoding: NotRequired[
        "aws_sdk_mediaconvert.types.h264_saliency_aware_encoding.H264SaliencyAwareEncoding"
    ]
    """Specify whether to apply Saliency aware encoding to your output. Use to improve the perceptual video quality of your output by allocating more encoding bits to the prominent or noticeable parts of your content. To apply saliency aware encoding, when possible: We recommend that you choose Preferred. The effects of Saliency aware encoding are best seen in lower bitrate outputs. When you choose Preferred, note that Saliency aware encoding will only apply to outputs that are 720p or higher in resolution. To not apply saliency aware encoding, prioritizing encoding speed over perceptual video quality: Choose Disabled."""
    scan_type_conversion_mode: NotRequired[
        "aws_sdk_mediaconvert.types.h264_scan_type_conversion_mode.H264ScanTypeConversionMode"
    ]
    """Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive."""
    scene_change_detect: NotRequired[
        "aws_sdk_mediaconvert.types.h264_scene_change_detect.H264SceneChangeDetect"
    ]
    """Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default. If this output uses QVBR, choose Transition detection for further video quality improvement. For more information about QVBR, see https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr."""
    slices: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max32.__integerMin1Max32"
    ]
    """Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures."""
    slow_pal: NotRequired["aws_sdk_mediaconvert.types.h264_slow_pal.H264SlowPal"]
    """Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25."""
    softness: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max128.__integerMin0Max128"
    ]
    """Ignore this setting unless you need to comply with a specification that requires a specific value. If you don't have a specification requirement, we recommend that you adjust the softness of your output by using a lower value for the setting Sharpness or by enabling a noise reducer filter. The Softness setting specifies the quantization matrices that the encoder uses. Keep the default value, 0, for flat quantization. Choose the value 1 or 16 to use the default JVT softening quantization matricies from the H.264 specification. Choose a value from 17 to 128 to use planar interpolation. Increasing values from 17 to 128 result in increasing reduction of high-frequency data. The value 128 results in the softest video."""
    spatial_adaptive_quantization: NotRequired[
        "aws_sdk_mediaconvert.types.h264_spatial_adaptive_quantization.H264SpatialAdaptiveQuantization"
    ]
    """Only use this setting when you change the default value, Auto, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264SpatialAdaptiveQuantization is Enabled. Keep this default value to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to set H264SpatialAdaptiveQuantization to Disabled. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher. To manually enable or disable H264SpatialAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO."""
    syntax: NotRequired["aws_sdk_mediaconvert.types.h264_syntax.H264Syntax"]
    """Produces a bitstream compliant with SMPTE RP-2027."""
    telecine: NotRequired["aws_sdk_mediaconvert.types.h264_telecine.H264Telecine"]
    """When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard or soft telecine to create a smoother picture. Hard telecine produces a 29.97i output. Soft telecine produces an output with a 23.976 output that signals to the video player device to do the conversion during play back. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture."""
    temporal_adaptive_quantization: NotRequired[
        "aws_sdk_mediaconvert.types.h264_temporal_adaptive_quantization.H264TemporalAdaptiveQuantization"
    ]
    """Only use this setting when you change the default value, AUTO, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264TemporalAdaptiveQuantization is Enabled. Keep this default value to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to set H264TemporalAdaptiveQuantization to Disabled. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization. To manually enable or disable H264TemporalAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO."""
    unregistered_sei_timecode: NotRequired[
        "aws_sdk_mediaconvert.types.h264_unregistered_sei_timecode.H264UnregisteredSeiTimecode"
    ]
    """Inserts timecode for each frame as 4 bytes of an unregistered SEI message."""
    write_mp4_packaging_type: NotRequired[
        "aws_sdk_mediaconvert.types.h264_write_mp4_packaging_type.H264WriteMp4PackagingType"
    ]
    """Specify how SPS and PPS NAL units are written in your output MP4 container, according to ISO/IEC 14496-15. If the location of these parameters doesn't matter in your workflow: Keep the default value, AVC1. MediaConvert writes SPS and PPS NAL units in the sample description ('stsd') box (but not into samples directly). To write SPS and PPS NAL units directly into samples (but not in the 'stsd' box): Choose AVC3. When you do, note that your output might not play properly with some downstream systems or players."""


# --- restJson1 ser/de ---
def serialize_json(value: H264Settings) -> dict:
    out: dict = {}
    if "adaptive_quantization" in value:
        import aws_sdk_mediaconvert.types.h264_adaptive_quantization

        out["adaptiveQuantization"] = (
            aws_sdk_mediaconvert.types.h264_adaptive_quantization.serialize_json(
                value["adaptive_quantization"]
            )
        )
    if "bandwidth_reduction_filter" in value:
        import aws_sdk_mediaconvert.types.bandwidth_reduction_filter

        out["bandwidthReductionFilter"] = (
            aws_sdk_mediaconvert.types.bandwidth_reduction_filter.serialize_json(
                value["bandwidth_reduction_filter"]
            )
        )
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "codec_level" in value:
        import aws_sdk_mediaconvert.types.h264_codec_level

        out["codecLevel"] = aws_sdk_mediaconvert.types.h264_codec_level.serialize_json(
            value["codec_level"]
        )
    if "codec_profile" in value:
        import aws_sdk_mediaconvert.types.h264_codec_profile

        out["codecProfile"] = (
            aws_sdk_mediaconvert.types.h264_codec_profile.serialize_json(
                value["codec_profile"]
            )
        )
    if "dynamic_sub_gop" in value:
        import aws_sdk_mediaconvert.types.h264_dynamic_sub_gop

        out["dynamicSubGop"] = (
            aws_sdk_mediaconvert.types.h264_dynamic_sub_gop.serialize_json(
                value["dynamic_sub_gop"]
            )
        )
    if "end_of_stream_markers" in value:
        import aws_sdk_mediaconvert.types.h264_end_of_stream_markers

        out["endOfStreamMarkers"] = (
            aws_sdk_mediaconvert.types.h264_end_of_stream_markers.serialize_json(
                value["end_of_stream_markers"]
            )
        )
    if "entropy_encoding" in value:
        import aws_sdk_mediaconvert.types.h264_entropy_encoding

        out["entropyEncoding"] = (
            aws_sdk_mediaconvert.types.h264_entropy_encoding.serialize_json(
                value["entropy_encoding"]
            )
        )
    if "field_encoding" in value:
        import aws_sdk_mediaconvert.types.h264_field_encoding

        out["fieldEncoding"] = (
            aws_sdk_mediaconvert.types.h264_field_encoding.serialize_json(
                value["field_encoding"]
            )
        )
    if "flicker_adaptive_quantization" in value:
        import aws_sdk_mediaconvert.types.h264_flicker_adaptive_quantization

        out["flickerAdaptiveQuantization"] = (
            aws_sdk_mediaconvert.types.h264_flicker_adaptive_quantization.serialize_json(
                value["flicker_adaptive_quantization"]
            )
        )
    if "framerate_control" in value:
        import aws_sdk_mediaconvert.types.h264_framerate_control

        out["framerateControl"] = (
            aws_sdk_mediaconvert.types.h264_framerate_control.serialize_json(
                value["framerate_control"]
            )
        )
    if "framerate_conversion_algorithm" in value:
        import aws_sdk_mediaconvert.types.h264_framerate_conversion_algorithm

        out["framerateConversionAlgorithm"] = (
            aws_sdk_mediaconvert.types.h264_framerate_conversion_algorithm.serialize_json(
                value["framerate_conversion_algorithm"]
            )
        )
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    if "gop_b_reference" in value:
        import aws_sdk_mediaconvert.types.h264_gop_b_reference

        out["gopBReference"] = (
            aws_sdk_mediaconvert.types.h264_gop_b_reference.serialize_json(
                value["gop_b_reference"]
            )
        )
    if "gop_closed_cadence" in value:
        out["gopClosedCadence"] = value["gop_closed_cadence"]
    if "gop_size" in value:
        out["gopSize"] = value["gop_size"]
    if "gop_size_units" in value:
        import aws_sdk_mediaconvert.types.h264_gop_size_units

        out["gopSizeUnits"] = (
            aws_sdk_mediaconvert.types.h264_gop_size_units.serialize_json(
                value["gop_size_units"]
            )
        )
    if "hrd_buffer_final_fill_percentage" in value:
        out["hrdBufferFinalFillPercentage"] = value["hrd_buffer_final_fill_percentage"]
    if "hrd_buffer_initial_fill_percentage" in value:
        out["hrdBufferInitialFillPercentage"] = value[
            "hrd_buffer_initial_fill_percentage"
        ]
    if "hrd_buffer_size" in value:
        out["hrdBufferSize"] = value["hrd_buffer_size"]
    if "interlace_mode" in value:
        import aws_sdk_mediaconvert.types.h264_interlace_mode

        out["interlaceMode"] = (
            aws_sdk_mediaconvert.types.h264_interlace_mode.serialize_json(
                value["interlace_mode"]
            )
        )
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "min_i_interval" in value:
        out["minIInterval"] = value["min_i_interval"]
    if "number_b_frames_between_reference_frames" in value:
        out["numberBFramesBetweenReferenceFrames"] = value[
            "number_b_frames_between_reference_frames"
        ]
    if "number_reference_frames" in value:
        out["numberReferenceFrames"] = value["number_reference_frames"]
    if "par_control" in value:
        import aws_sdk_mediaconvert.types.h264_par_control

        out["parControl"] = aws_sdk_mediaconvert.types.h264_par_control.serialize_json(
            value["par_control"]
        )
    if "par_denominator" in value:
        out["parDenominator"] = value["par_denominator"]
    if "par_numerator" in value:
        out["parNumerator"] = value["par_numerator"]
    if "per_frame_metrics" in value:
        import aws_sdk_mediaconvert.types.__list_of_frame_metric_type

        out["perFrameMetrics"] = (
            aws_sdk_mediaconvert.types.__list_of_frame_metric_type.serialize_json(
                value["per_frame_metrics"]
            )
        )
    if "quality_tuning_level" in value:
        import aws_sdk_mediaconvert.types.h264_quality_tuning_level

        out["qualityTuningLevel"] = (
            aws_sdk_mediaconvert.types.h264_quality_tuning_level.serialize_json(
                value["quality_tuning_level"]
            )
        )
    if "qvbr_settings" in value:
        import aws_sdk_mediaconvert.types.h264_qvbr_settings

        out["qvbrSettings"] = (
            aws_sdk_mediaconvert.types.h264_qvbr_settings.serialize_json(
                value["qvbr_settings"]
            )
        )
    if "rate_control_mode" in value:
        import aws_sdk_mediaconvert.types.h264_rate_control_mode

        out["rateControlMode"] = (
            aws_sdk_mediaconvert.types.h264_rate_control_mode.serialize_json(
                value["rate_control_mode"]
            )
        )
    if "repeat_pps" in value:
        import aws_sdk_mediaconvert.types.h264_repeat_pps

        out["repeatPps"] = aws_sdk_mediaconvert.types.h264_repeat_pps.serialize_json(
            value["repeat_pps"]
        )
    if "saliency_aware_encoding" in value:
        import aws_sdk_mediaconvert.types.h264_saliency_aware_encoding

        out["saliencyAwareEncoding"] = (
            aws_sdk_mediaconvert.types.h264_saliency_aware_encoding.serialize_json(
                value["saliency_aware_encoding"]
            )
        )
    if "scan_type_conversion_mode" in value:
        import aws_sdk_mediaconvert.types.h264_scan_type_conversion_mode

        out["scanTypeConversionMode"] = (
            aws_sdk_mediaconvert.types.h264_scan_type_conversion_mode.serialize_json(
                value["scan_type_conversion_mode"]
            )
        )
    if "scene_change_detect" in value:
        import aws_sdk_mediaconvert.types.h264_scene_change_detect

        out["sceneChangeDetect"] = (
            aws_sdk_mediaconvert.types.h264_scene_change_detect.serialize_json(
                value["scene_change_detect"]
            )
        )
    if "slices" in value:
        out["slices"] = value["slices"]
    if "slow_pal" in value:
        import aws_sdk_mediaconvert.types.h264_slow_pal

        out["slowPal"] = aws_sdk_mediaconvert.types.h264_slow_pal.serialize_json(
            value["slow_pal"]
        )
    if "softness" in value:
        out["softness"] = value["softness"]
    if "spatial_adaptive_quantization" in value:
        import aws_sdk_mediaconvert.types.h264_spatial_adaptive_quantization

        out["spatialAdaptiveQuantization"] = (
            aws_sdk_mediaconvert.types.h264_spatial_adaptive_quantization.serialize_json(
                value["spatial_adaptive_quantization"]
            )
        )
    if "syntax" in value:
        import aws_sdk_mediaconvert.types.h264_syntax

        out["syntax"] = aws_sdk_mediaconvert.types.h264_syntax.serialize_json(
            value["syntax"]
        )
    if "telecine" in value:
        import aws_sdk_mediaconvert.types.h264_telecine

        out["telecine"] = aws_sdk_mediaconvert.types.h264_telecine.serialize_json(
            value["telecine"]
        )
    if "temporal_adaptive_quantization" in value:
        import aws_sdk_mediaconvert.types.h264_temporal_adaptive_quantization

        out["temporalAdaptiveQuantization"] = (
            aws_sdk_mediaconvert.types.h264_temporal_adaptive_quantization.serialize_json(
                value["temporal_adaptive_quantization"]
            )
        )
    if "unregistered_sei_timecode" in value:
        import aws_sdk_mediaconvert.types.h264_unregistered_sei_timecode

        out["unregisteredSeiTimecode"] = (
            aws_sdk_mediaconvert.types.h264_unregistered_sei_timecode.serialize_json(
                value["unregistered_sei_timecode"]
            )
        )
    if "write_mp4_packaging_type" in value:
        import aws_sdk_mediaconvert.types.h264_write_mp4_packaging_type

        out["writeMp4PackagingType"] = (
            aws_sdk_mediaconvert.types.h264_write_mp4_packaging_type.serialize_json(
                value["write_mp4_packaging_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> H264Settings:
    out: H264Settings = {}  # type: ignore[typeddict-item]
    if "adaptiveQuantization" in data:
        import aws_sdk_mediaconvert.types.h264_adaptive_quantization

        out["adaptive_quantization"] = (
            aws_sdk_mediaconvert.types.h264_adaptive_quantization.deserialize_json(
                data["adaptiveQuantization"]
            )
        )
    if "bandwidthReductionFilter" in data:
        import aws_sdk_mediaconvert.types.bandwidth_reduction_filter

        out["bandwidth_reduction_filter"] = (
            aws_sdk_mediaconvert.types.bandwidth_reduction_filter.deserialize_json(
                data["bandwidthReductionFilter"]
            )
        )
    if "bitrate" in data:
        out["bitrate"] = data["bitrate"]
    if "codecLevel" in data:
        import aws_sdk_mediaconvert.types.h264_codec_level

        out["codec_level"] = (
            aws_sdk_mediaconvert.types.h264_codec_level.deserialize_json(
                data["codecLevel"]
            )
        )
    if "codecProfile" in data:
        import aws_sdk_mediaconvert.types.h264_codec_profile

        out["codec_profile"] = (
            aws_sdk_mediaconvert.types.h264_codec_profile.deserialize_json(
                data["codecProfile"]
            )
        )
    if "dynamicSubGop" in data:
        import aws_sdk_mediaconvert.types.h264_dynamic_sub_gop

        out["dynamic_sub_gop"] = (
            aws_sdk_mediaconvert.types.h264_dynamic_sub_gop.deserialize_json(
                data["dynamicSubGop"]
            )
        )
    if "endOfStreamMarkers" in data:
        import aws_sdk_mediaconvert.types.h264_end_of_stream_markers

        out["end_of_stream_markers"] = (
            aws_sdk_mediaconvert.types.h264_end_of_stream_markers.deserialize_json(
                data["endOfStreamMarkers"]
            )
        )
    if "entropyEncoding" in data:
        import aws_sdk_mediaconvert.types.h264_entropy_encoding

        out["entropy_encoding"] = (
            aws_sdk_mediaconvert.types.h264_entropy_encoding.deserialize_json(
                data["entropyEncoding"]
            )
        )
    if "fieldEncoding" in data:
        import aws_sdk_mediaconvert.types.h264_field_encoding

        out["field_encoding"] = (
            aws_sdk_mediaconvert.types.h264_field_encoding.deserialize_json(
                data["fieldEncoding"]
            )
        )
    if "flickerAdaptiveQuantization" in data:
        import aws_sdk_mediaconvert.types.h264_flicker_adaptive_quantization

        out["flicker_adaptive_quantization"] = (
            aws_sdk_mediaconvert.types.h264_flicker_adaptive_quantization.deserialize_json(
                data["flickerAdaptiveQuantization"]
            )
        )
    if "framerateControl" in data:
        import aws_sdk_mediaconvert.types.h264_framerate_control

        out["framerate_control"] = (
            aws_sdk_mediaconvert.types.h264_framerate_control.deserialize_json(
                data["framerateControl"]
            )
        )
    if "framerateConversionAlgorithm" in data:
        import aws_sdk_mediaconvert.types.h264_framerate_conversion_algorithm

        out["framerate_conversion_algorithm"] = (
            aws_sdk_mediaconvert.types.h264_framerate_conversion_algorithm.deserialize_json(
                data["framerateConversionAlgorithm"]
            )
        )
    if "framerateDenominator" in data:
        out["framerate_denominator"] = data["framerateDenominator"]
    if "framerateNumerator" in data:
        out["framerate_numerator"] = data["framerateNumerator"]
    if "gopBReference" in data:
        import aws_sdk_mediaconvert.types.h264_gop_b_reference

        out["gop_b_reference"] = (
            aws_sdk_mediaconvert.types.h264_gop_b_reference.deserialize_json(
                data["gopBReference"]
            )
        )
    if "gopClosedCadence" in data:
        out["gop_closed_cadence"] = data["gopClosedCadence"]
    if "gopSize" in data:
        out["gop_size"] = data["gopSize"]
    if "gopSizeUnits" in data:
        import aws_sdk_mediaconvert.types.h264_gop_size_units

        out["gop_size_units"] = (
            aws_sdk_mediaconvert.types.h264_gop_size_units.deserialize_json(
                data["gopSizeUnits"]
            )
        )
    if "hrdBufferFinalFillPercentage" in data:
        out["hrd_buffer_final_fill_percentage"] = data["hrdBufferFinalFillPercentage"]
    if "hrdBufferInitialFillPercentage" in data:
        out["hrd_buffer_initial_fill_percentage"] = data[
            "hrdBufferInitialFillPercentage"
        ]
    if "hrdBufferSize" in data:
        out["hrd_buffer_size"] = data["hrdBufferSize"]
    if "interlaceMode" in data:
        import aws_sdk_mediaconvert.types.h264_interlace_mode

        out["interlace_mode"] = (
            aws_sdk_mediaconvert.types.h264_interlace_mode.deserialize_json(
                data["interlaceMode"]
            )
        )
    if "maxBitrate" in data:
        out["max_bitrate"] = data["maxBitrate"]
    if "minIInterval" in data:
        out["min_i_interval"] = data["minIInterval"]
    if "numberBFramesBetweenReferenceFrames" in data:
        out["number_b_frames_between_reference_frames"] = data[
            "numberBFramesBetweenReferenceFrames"
        ]
    if "numberReferenceFrames" in data:
        out["number_reference_frames"] = data["numberReferenceFrames"]
    if "parControl" in data:
        import aws_sdk_mediaconvert.types.h264_par_control

        out["par_control"] = (
            aws_sdk_mediaconvert.types.h264_par_control.deserialize_json(
                data["parControl"]
            )
        )
    if "parDenominator" in data:
        out["par_denominator"] = data["parDenominator"]
    if "parNumerator" in data:
        out["par_numerator"] = data["parNumerator"]
    if "perFrameMetrics" in data:
        import aws_sdk_mediaconvert.types.__list_of_frame_metric_type

        out["per_frame_metrics"] = (
            aws_sdk_mediaconvert.types.__list_of_frame_metric_type.deserialize_json(
                data["perFrameMetrics"]
            )
        )
    if "qualityTuningLevel" in data:
        import aws_sdk_mediaconvert.types.h264_quality_tuning_level

        out["quality_tuning_level"] = (
            aws_sdk_mediaconvert.types.h264_quality_tuning_level.deserialize_json(
                data["qualityTuningLevel"]
            )
        )
    if "qvbrSettings" in data:
        import aws_sdk_mediaconvert.types.h264_qvbr_settings

        out["qvbr_settings"] = (
            aws_sdk_mediaconvert.types.h264_qvbr_settings.deserialize_json(
                data["qvbrSettings"]
            )
        )
    if "rateControlMode" in data:
        import aws_sdk_mediaconvert.types.h264_rate_control_mode

        out["rate_control_mode"] = (
            aws_sdk_mediaconvert.types.h264_rate_control_mode.deserialize_json(
                data["rateControlMode"]
            )
        )
    if "repeatPps" in data:
        import aws_sdk_mediaconvert.types.h264_repeat_pps

        out["repeat_pps"] = aws_sdk_mediaconvert.types.h264_repeat_pps.deserialize_json(
            data["repeatPps"]
        )
    if "saliencyAwareEncoding" in data:
        import aws_sdk_mediaconvert.types.h264_saliency_aware_encoding

        out["saliency_aware_encoding"] = (
            aws_sdk_mediaconvert.types.h264_saliency_aware_encoding.deserialize_json(
                data["saliencyAwareEncoding"]
            )
        )
    if "scanTypeConversionMode" in data:
        import aws_sdk_mediaconvert.types.h264_scan_type_conversion_mode

        out["scan_type_conversion_mode"] = (
            aws_sdk_mediaconvert.types.h264_scan_type_conversion_mode.deserialize_json(
                data["scanTypeConversionMode"]
            )
        )
    if "sceneChangeDetect" in data:
        import aws_sdk_mediaconvert.types.h264_scene_change_detect

        out["scene_change_detect"] = (
            aws_sdk_mediaconvert.types.h264_scene_change_detect.deserialize_json(
                data["sceneChangeDetect"]
            )
        )
    if "slices" in data:
        out["slices"] = data["slices"]
    if "slowPal" in data:
        import aws_sdk_mediaconvert.types.h264_slow_pal

        out["slow_pal"] = aws_sdk_mediaconvert.types.h264_slow_pal.deserialize_json(
            data["slowPal"]
        )
    if "softness" in data:
        out["softness"] = data["softness"]
    if "spatialAdaptiveQuantization" in data:
        import aws_sdk_mediaconvert.types.h264_spatial_adaptive_quantization

        out["spatial_adaptive_quantization"] = (
            aws_sdk_mediaconvert.types.h264_spatial_adaptive_quantization.deserialize_json(
                data["spatialAdaptiveQuantization"]
            )
        )
    if "syntax" in data:
        import aws_sdk_mediaconvert.types.h264_syntax

        out["syntax"] = aws_sdk_mediaconvert.types.h264_syntax.deserialize_json(
            data["syntax"]
        )
    if "telecine" in data:
        import aws_sdk_mediaconvert.types.h264_telecine

        out["telecine"] = aws_sdk_mediaconvert.types.h264_telecine.deserialize_json(
            data["telecine"]
        )
    if "temporalAdaptiveQuantization" in data:
        import aws_sdk_mediaconvert.types.h264_temporal_adaptive_quantization

        out["temporal_adaptive_quantization"] = (
            aws_sdk_mediaconvert.types.h264_temporal_adaptive_quantization.deserialize_json(
                data["temporalAdaptiveQuantization"]
            )
        )
    if "unregisteredSeiTimecode" in data:
        import aws_sdk_mediaconvert.types.h264_unregistered_sei_timecode

        out["unregistered_sei_timecode"] = (
            aws_sdk_mediaconvert.types.h264_unregistered_sei_timecode.deserialize_json(
                data["unregisteredSeiTimecode"]
            )
        )
    if "writeMp4PackagingType" in data:
        import aws_sdk_mediaconvert.types.h264_write_mp4_packaging_type

        out["write_mp4_packaging_type"] = (
            aws_sdk_mediaconvert.types.h264_write_mp4_packaging_type.deserialize_json(
                data["writeMp4PackagingType"]
            )
        )
    return out
