"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DependentEntity``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn_list
    import aws_sdk_ssm_contacts.types.string


class DependentEntity(TypedDict):
    relation_type: "aws_sdk_ssm_contacts.types.string.String"
    """<p>The type of relationship between one resource and the other resource that it is related to or depends on.</p>"""
    dependent_resource_ids: (
        "aws_sdk_ssm_contacts.types.ssm_contacts_arn_list.SsmContactsArnList"
    )
    """<p>The Amazon Resource Names (ARNs) of the dependent resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DependentEntity) -> dict:
    out: dict = {}
    out["RelationType"] = value["relation_type"]
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn_list

    out["DependentResourceIds"] = (
        aws_sdk_ssm_contacts.types.ssm_contacts_arn_list.serialize_aws_json_1_1(
            value["dependent_resource_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DependentEntity:
    out: DependentEntity = {}  # type: ignore[typeddict-item]
    if "RelationType" in data:
        out["relation_type"] = data["RelationType"]
    else:
        raise DeserializationError("DependentEntity.relation_type required")
    if "DependentResourceIds" in data:
        import aws_sdk_ssm_contacts.types.ssm_contacts_arn_list

        out["dependent_resource_ids"] = (
            aws_sdk_ssm_contacts.types.ssm_contacts_arn_list.deserialize_aws_json_1_1(
                data["DependentResourceIds"]
            )
        )
    else:
        raise DeserializationError("DependentEntity.dependent_resource_ids required")
    return out
