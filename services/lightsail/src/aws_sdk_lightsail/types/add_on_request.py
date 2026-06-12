"""Generated from Smithy shape ``com.amazonaws.lightsail#AddOnRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.add_on_type
    import aws_sdk_lightsail.types.auto_snapshot_add_on_request
    import aws_sdk_lightsail.types.stop_instance_on_idle_request


class AddOnRequest(TypedDict):
    add_on_type: "aws_sdk_lightsail.types.add_on_type.AddOnType"
    """<p>The add-on type.</p>"""
    auto_snapshot_add_on_request: NotRequired[
        "aws_sdk_lightsail.types.auto_snapshot_add_on_request.AutoSnapshotAddOnRequest"
    ]
    """<p>An object that represents additional parameters when enabling or modifying the automatic snapshot add-on.</p>"""
    stop_instance_on_idle_request: NotRequired[
        "aws_sdk_lightsail.types.stop_instance_on_idle_request.StopInstanceOnIdleRequest"
    ]
    """<p>An object that represents additional parameters when enabling or modifying the <code>StopInstanceOnIdle</code> add-on.</p> <important> <p>This object only applies to Lightsail for Research resources.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddOnRequest) -> dict:
    out: dict = {}
    import aws_sdk_lightsail.types.add_on_type

    out["addOnType"] = aws_sdk_lightsail.types.add_on_type.serialize_aws_json_1_1(
        value["add_on_type"]
    )
    if "auto_snapshot_add_on_request" in value:
        import aws_sdk_lightsail.types.auto_snapshot_add_on_request

        out["autoSnapshotAddOnRequest"] = (
            aws_sdk_lightsail.types.auto_snapshot_add_on_request.serialize_aws_json_1_1(
                value["auto_snapshot_add_on_request"]
            )
        )
    if "stop_instance_on_idle_request" in value:
        import aws_sdk_lightsail.types.stop_instance_on_idle_request

        out["stopInstanceOnIdleRequest"] = (
            aws_sdk_lightsail.types.stop_instance_on_idle_request.serialize_aws_json_1_1(
                value["stop_instance_on_idle_request"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddOnRequest:
    out: AddOnRequest = {}  # type: ignore[typeddict-item]
    if "addOnType" in data:
        import aws_sdk_lightsail.types.add_on_type

        out["add_on_type"] = (
            aws_sdk_lightsail.types.add_on_type.deserialize_aws_json_1_1(
                data["addOnType"]
            )
        )
    else:
        raise DeserializationError("AddOnRequest.add_on_type required")
    if "autoSnapshotAddOnRequest" in data:
        import aws_sdk_lightsail.types.auto_snapshot_add_on_request

        out["auto_snapshot_add_on_request"] = (
            aws_sdk_lightsail.types.auto_snapshot_add_on_request.deserialize_aws_json_1_1(
                data["autoSnapshotAddOnRequest"]
            )
        )
    if "stopInstanceOnIdleRequest" in data:
        import aws_sdk_lightsail.types.stop_instance_on_idle_request

        out["stop_instance_on_idle_request"] = (
            aws_sdk_lightsail.types.stop_instance_on_idle_request.deserialize_aws_json_1_1(
                data["stopInstanceOnIdleRequest"]
            )
        )
    return out
