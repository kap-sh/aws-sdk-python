"""Generated from Smithy shape ``com.amazonaws.identitystore#ExternalIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.external_id

ExternalIds: TypeAlias = list["capo_identitystore.types.external_id.ExternalId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExternalIds) -> list:
    import capo_identitystore.types.external_id

    out: list = []
    for item in value:
        out.append(capo_identitystore.types.external_id.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExternalIds:
    import capo_identitystore.types.external_id

    out: ExternalIds = []
    for item in data:
        out.append(capo_identitystore.types.external_id.deserialize_aws_json_1_1(item))
    return out
