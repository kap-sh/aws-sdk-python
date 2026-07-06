"""Generated from Smithy shape ``com.amazonaws.rds#Timezone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class Timezone(TypedDict, closed=True):
    timezone_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the time zone.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Timezone, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "timezone_name" in value:
        pairs.append((f"{prefix}.TimezoneName", str(value["timezone_name"])))


def deserialize_query(el: Element) -> Timezone:
    out: Timezone = {}  # type: ignore[typeddict-item]
    child_timezone_name = el.find("TimezoneName")
    if child_timezone_name is not None:
        out["timezone_name"] = str(child_timezone_name.text or "")
    return out
