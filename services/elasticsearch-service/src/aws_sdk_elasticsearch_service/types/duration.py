"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#Duration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.duration_value
    import aws_sdk_elasticsearch_service.types.time_unit


class Duration(TypedDict):
    value: NotRequired[
        "aws_sdk_elasticsearch_service.types.duration_value.DurationValue"
    ]
    """<p> Integer to specify the value of a maintenance schedule duration. See the <a href=\"https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html\" target=\"_blank\">Developer Guide</a> for more information.</p>"""
    unit: NotRequired["aws_sdk_elasticsearch_service.types.time_unit.TimeUnit"]
    """<p>Specifies the unit of a maintenance schedule duration. Valid value is HOURS. See the <a href=\"https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html\" target=\"_blank\">Developer Guide</a> for more information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Duration) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "unit" in value:
        import aws_sdk_elasticsearch_service.types.time_unit

        out["Unit"] = aws_sdk_elasticsearch_service.types.time_unit.serialize_json(
            value["unit"]
        )
    return out


def deserialize_json(data: dict) -> Duration:
    out: Duration = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Unit" in data:
        import aws_sdk_elasticsearch_service.types.time_unit

        out["unit"] = aws_sdk_elasticsearch_service.types.time_unit.deserialize_json(
            data["Unit"]
        )
    return out
