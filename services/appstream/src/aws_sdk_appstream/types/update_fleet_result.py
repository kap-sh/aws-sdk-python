"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateFleetResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.fleet


class UpdateFleetResult(TypedDict):
    fleet: NotRequired["aws_sdk_appstream.types.fleet.Fleet"]
    """<p>Information about the fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFleetResult) -> dict:
    out: dict = {}
    if "fleet" in value:
        import aws_sdk_appstream.types.fleet

        out["Fleet"] = aws_sdk_appstream.types.fleet.serialize_aws_json_1_1(
            value["fleet"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFleetResult:
    out: UpdateFleetResult = {}  # type: ignore[typeddict-item]
    if "Fleet" in data:
        import aws_sdk_appstream.types.fleet

        out["fleet"] = aws_sdk_appstream.types.fleet.deserialize_aws_json_1_1(
            data["Fleet"]
        )
    return out
