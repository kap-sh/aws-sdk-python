"""Generated from Smithy shape ``com.amazonaws.odb#DayOfWeek``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_odb.types.day_of_week_name


class DayOfWeek(TypedDict):
    name: NotRequired["aws_sdk_odb.types.day_of_week_name.DayOfWeekName"]
    """<p>The name of the day of the week.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DayOfWeek) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_odb.types.day_of_week_name

        out["name"] = aws_sdk_odb.types.day_of_week_name.serialize_aws_json_1_0(
            value["name"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DayOfWeek:
    out: DayOfWeek = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_odb.types.day_of_week_name

        out["name"] = aws_sdk_odb.types.day_of_week_name.deserialize_aws_json_1_0(
            data["name"]
        )
    return out
