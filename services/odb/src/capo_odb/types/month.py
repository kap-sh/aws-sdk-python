"""Generated from Smithy shape ``com.amazonaws.odb#Month``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.month_name


class Month(TypedDict, closed=True):
    name: NotRequired["capo_odb.types.month_name.MonthName"]
    """<p>The name of the month.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Month) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_odb.types.month_name

        out["name"] = capo_odb.types.month_name.serialize_aws_json_1_0(value["name"])
    return out


def deserialize_aws_json_1_0(data: dict) -> Month:
    out: Month = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import capo_odb.types.month_name

        out["name"] = capo_odb.types.month_name.deserialize_aws_json_1_0(data["name"])
    return out
