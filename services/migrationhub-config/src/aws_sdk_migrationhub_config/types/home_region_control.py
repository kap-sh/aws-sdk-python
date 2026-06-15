"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#HomeRegionControl``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhub_config.types.control_id
    import aws_sdk_migrationhub_config.types.home_region
    import aws_sdk_migrationhub_config.types.requested_time
    import aws_sdk_migrationhub_config.types.target


class HomeRegionControl(TypedDict):
    control_id: NotRequired["aws_sdk_migrationhub_config.types.control_id.ControlId"]
    r"""<p>A unique identifier that's generated for each home region control. It's always a string that begins with \"hrc-\" followed by 12 lowercase letters and numbers.</p>"""
    home_region: NotRequired["aws_sdk_migrationhub_config.types.home_region.HomeRegion"]
    r"""<p>The AWS Region that's been set as home region. For example, \"us-west-2\" or \"eu-central-1\" are valid home regions.</p>"""
    target: NotRequired["aws_sdk_migrationhub_config.types.target.Target"]
    """<p>The target parameter specifies the identifier to which the home region is applied, which is always an <code>ACCOUNT</code>. It applies the home region to the current <code>ACCOUNT</code>.</p>"""
    requested_time: NotRequired[
        "aws_sdk_migrationhub_config.types.requested_time.RequestedTime"
    ]
    """<p>A timestamp representing the time when the customer called <code>CreateHomeregionControl</code> and set the home region for the account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HomeRegionControl) -> dict:
    out: dict = {}
    if "control_id" in value:
        out["ControlId"] = value["control_id"]
    if "home_region" in value:
        out["HomeRegion"] = value["home_region"]
    if "target" in value:
        import aws_sdk_migrationhub_config.types.target

        out["Target"] = aws_sdk_migrationhub_config.types.target.serialize_aws_json_1_1(
            value["target"]
        )
    if "requested_time" in value:
        import aws_sdk_migrationhub_config.types.requested_time

        out["RequestedTime"] = (
            aws_sdk_migrationhub_config.types.requested_time.serialize_aws_json_1_1(
                value["requested_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HomeRegionControl:
    out: HomeRegionControl = {}  # type: ignore[typeddict-item]
    if "ControlId" in data:
        out["control_id"] = data["ControlId"]
    if "HomeRegion" in data:
        out["home_region"] = data["HomeRegion"]
    if "Target" in data:
        import aws_sdk_migrationhub_config.types.target

        out["target"] = (
            aws_sdk_migrationhub_config.types.target.deserialize_aws_json_1_1(
                data["Target"]
            )
        )
    if "RequestedTime" in data:
        import aws_sdk_migrationhub_config.types.requested_time

        out["requested_time"] = (
            aws_sdk_migrationhub_config.types.requested_time.deserialize_aws_json_1_1(
                data["RequestedTime"]
            )
        )
    return out
