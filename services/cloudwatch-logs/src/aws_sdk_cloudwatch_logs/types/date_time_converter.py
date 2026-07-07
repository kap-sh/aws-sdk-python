"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DateTimeConverter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.locale
    import aws_sdk_cloudwatch_logs.types.match_patterns
    import aws_sdk_cloudwatch_logs.types.source
    import aws_sdk_cloudwatch_logs.types.source_timezone
    import aws_sdk_cloudwatch_logs.types.target
    import aws_sdk_cloudwatch_logs.types.target_format
    import aws_sdk_cloudwatch_logs.types.target_timezone


class DateTimeConverter(TypedDict, closed=True):
    source: "aws_sdk_cloudwatch_logs.types.source.Source"
    """<p>The key to apply the date conversion to.</p>"""
    target: "aws_sdk_cloudwatch_logs.types.target.Target"
    """<p>The JSON field to store the result in.</p>"""
    target_format: NotRequired[
        "aws_sdk_cloudwatch_logs.types.target_format.TargetFormat"
    ]
    """<p>The datetime format to use for the converted data in the target field.</p> <p>If you omit this, the default of <code> yyyy-MM-dd'T'HH:mm:ss.SSS'Z</code> is used.</p>"""
    match_patterns: "aws_sdk_cloudwatch_logs.types.match_patterns.MatchPatterns"
    """<p>A list of patterns to match against the <code>source</code> field.</p>"""
    source_timezone: NotRequired[
        "aws_sdk_cloudwatch_logs.types.source_timezone.SourceTimezone"
    ]
    """<p>The time zone of the source field. If you omit this, the default used is the UTC zone.</p>"""
    target_timezone: NotRequired[
        "aws_sdk_cloudwatch_logs.types.target_timezone.TargetTimezone"
    ]
    """<p>The time zone of the target field. If you omit this, the default used is the UTC zone.</p>"""
    locale: NotRequired["aws_sdk_cloudwatch_logs.types.locale.Locale"]
    """<p>The locale of the source field. If you omit this, the default of <code>locale.ROOT</code> is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DateTimeConverter) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["target"] = value["target"]
    if "target_format" in value:
        out["targetFormat"] = value["target_format"]
    import aws_sdk_cloudwatch_logs.types.match_patterns

    out["matchPatterns"] = (
        aws_sdk_cloudwatch_logs.types.match_patterns.serialize_aws_json_1_1(
            value["match_patterns"]
        )
    )
    if "source_timezone" in value:
        out["sourceTimezone"] = value["source_timezone"]
    if "target_timezone" in value:
        out["targetTimezone"] = value["target_timezone"]
    if "locale" in value:
        out["locale"] = value["locale"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DateTimeConverter:
    out: DateTimeConverter = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("DateTimeConverter.source required")
    if "target" in data:
        out["target"] = data["target"]
    else:
        raise DeserializationError("DateTimeConverter.target required")
    if "targetFormat" in data:
        out["target_format"] = data["targetFormat"]
    if "matchPatterns" in data:
        import aws_sdk_cloudwatch_logs.types.match_patterns

        out["match_patterns"] = (
            aws_sdk_cloudwatch_logs.types.match_patterns.deserialize_aws_json_1_1(
                data["matchPatterns"]
            )
        )
    else:
        raise DeserializationError("DateTimeConverter.match_patterns required")
    if "sourceTimezone" in data:
        out["source_timezone"] = data["sourceTimezone"]
    if "targetTimezone" in data:
        out["target_timezone"] = data["targetTimezone"]
    if "locale" in data:
        out["locale"] = data["locale"]
    return out
