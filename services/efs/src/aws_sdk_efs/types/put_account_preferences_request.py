"""Generated from Smithy shape ``com.amazonaws.efs#PutAccountPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_efs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_efs.types.resource_id_type


class PutAccountPreferencesRequest(TypedDict, closed=True):
    resource_id_type: "aws_sdk_efs.types.resource_id_type.ResourceIdType"
    """<p>Specifies the EFS resource ID preference to set for the user's Amazon Web Services account, in the current Amazon Web Services Region, either <code>LONG_ID</code> (17 characters), or <code>SHORT_ID</code> (8 characters).</p> <note> <p>Starting in October, 2021, you will receive an error when setting the account preference to <code>SHORT_ID</code>. Contact Amazon Web Services support if you receive an error and must use short IDs for file system and mount target resources.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountPreferencesRequest) -> dict:
    out: dict = {}
    import aws_sdk_efs.types.resource_id_type

    out["ResourceIdType"] = aws_sdk_efs.types.resource_id_type.serialize_json(
        value["resource_id_type"]
    )
    return out


def deserialize_json(data: dict) -> PutAccountPreferencesRequest:
    out: PutAccountPreferencesRequest = {}  # type: ignore[typeddict-item]
    if "ResourceIdType" in data:
        import aws_sdk_efs.types.resource_id_type

        out["resource_id_type"] = aws_sdk_efs.types.resource_id_type.deserialize_json(
            data["ResourceIdType"]
        )
    else:
        raise DeserializationError(
            "PutAccountPreferencesRequest.resource_id_type required"
        )
    return out
