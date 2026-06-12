"""Generated from Smithy shape ``com.amazonaws.ssm#StartAssociationsOnceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_id_list


class StartAssociationsOnceRequest(TypedDict):
    association_ids: "aws_sdk_ssm.types.association_id_list.AssociationIdList"
    """<p>The association IDs that you want to run immediately and only one time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartAssociationsOnceRequest) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.association_id_list

    out["AssociationIds"] = (
        aws_sdk_ssm.types.association_id_list.serialize_aws_json_1_1(
            value["association_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartAssociationsOnceRequest:
    out: StartAssociationsOnceRequest = {}  # type: ignore[typeddict-item]
    if "AssociationIds" in data:
        import aws_sdk_ssm.types.association_id_list

        out["association_ids"] = (
            aws_sdk_ssm.types.association_id_list.deserialize_aws_json_1_1(
                data["AssociationIds"]
            )
        )
    else:
        raise DeserializationError(
            "StartAssociationsOnceRequest.association_ids required"
        )
    return out
