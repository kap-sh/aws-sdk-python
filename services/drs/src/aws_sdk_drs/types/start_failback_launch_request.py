"""Generated from Smithy shape ``com.amazonaws.drs#StartFailbackLaunchRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.start_failback_request_recovery_instance_i_ds
    import aws_sdk_drs.types.tags_map


class StartFailbackLaunchRequest(TypedDict):
    recovery_instance_i_ds: "aws_sdk_drs.types.start_failback_request_recovery_instance_i_ds.StartFailbackRequestRecoveryInstanceIDs"
    """<p>The IDs of the Recovery Instance whose failback launch we want to request.</p>"""
    tags: NotRequired["aws_sdk_drs.types.tags_map.TagsMap"]
    """<p>The tags to be associated with the failback launch Job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartFailbackLaunchRequest) -> dict:
    out: dict = {}
    import aws_sdk_drs.types.start_failback_request_recovery_instance_i_ds

    out["recoveryInstanceIDs"] = (
        aws_sdk_drs.types.start_failback_request_recovery_instance_i_ds.serialize_json(
            value["recovery_instance_i_ds"]
        )
    )
    if "tags" in value:
        import aws_sdk_drs.types.tags_map

        out["tags"] = aws_sdk_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartFailbackLaunchRequest:
    out: StartFailbackLaunchRequest = {}  # type: ignore[typeddict-item]
    if "recoveryInstanceIDs" in data:
        import aws_sdk_drs.types.start_failback_request_recovery_instance_i_ds

        out["recovery_instance_i_ds"] = (
            aws_sdk_drs.types.start_failback_request_recovery_instance_i_ds.deserialize_json(
                data["recoveryInstanceIDs"]
            )
        )
    else:
        raise DeserializationError(
            "StartFailbackLaunchRequest.recovery_instance_i_ds required"
        )
    if "tags" in data:
        import aws_sdk_drs.types.tags_map

        out["tags"] = aws_sdk_drs.types.tags_map.deserialize_json(data["tags"])
    return out
