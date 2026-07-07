"""Generated from Smithy shape ``com.amazonaws.licensemanager#AutomatedDiscoveryInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.date_time


class AutomatedDiscoveryInformation(TypedDict, closed=True):
    last_run_time: NotRequired["aws_sdk_license_manager.types.date_time.DateTime"]
    """<p>Time that automated discovery last ran.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomatedDiscoveryInformation) -> dict:
    out: dict = {}
    if "last_run_time" in value:
        import aws_sdk_license_manager.types.date_time

        out["LastRunTime"] = (
            aws_sdk_license_manager.types.date_time.serialize_aws_json_1_1(
                value["last_run_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutomatedDiscoveryInformation:
    out: AutomatedDiscoveryInformation = {}  # type: ignore[typeddict-item]
    if "LastRunTime" in data:
        import aws_sdk_license_manager.types.date_time

        out["last_run_time"] = (
            aws_sdk_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["LastRunTime"]
            )
        )
    return out
