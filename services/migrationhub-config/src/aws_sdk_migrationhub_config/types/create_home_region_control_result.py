"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#CreateHomeRegionControlResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhub_config.types.home_region_control


class CreateHomeRegionControlResult(TypedDict):
    home_region_control: NotRequired[
        "aws_sdk_migrationhub_config.types.home_region_control.HomeRegionControl"
    ]
    """<p>This object is the <code>HomeRegionControl</code> object that's returned by a successful call to <code>CreateHomeRegionControl</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHomeRegionControlResult) -> dict:
    out: dict = {}
    if "home_region_control" in value:
        import aws_sdk_migrationhub_config.types.home_region_control

        out["HomeRegionControl"] = (
            aws_sdk_migrationhub_config.types.home_region_control.serialize_aws_json_1_1(
                value["home_region_control"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHomeRegionControlResult:
    out: CreateHomeRegionControlResult = {}  # type: ignore[typeddict-item]
    if "HomeRegionControl" in data:
        import aws_sdk_migrationhub_config.types.home_region_control

        out["home_region_control"] = (
            aws_sdk_migrationhub_config.types.home_region_control.deserialize_aws_json_1_1(
                data["HomeRegionControl"]
            )
        )
    return out
