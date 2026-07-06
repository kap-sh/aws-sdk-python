"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PutSchemaOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.namespace_list
    import aws_sdk_verifiedpermissions.types.policy_store_id
    import aws_sdk_verifiedpermissions.types.timestamp_format


class PutSchemaOutput(TypedDict, closed=True):
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The unique ID of the policy store that contains the schema.</p>"""
    namespaces: "aws_sdk_verifiedpermissions.types.namespace_list.NamespaceList"
    """<p>Identifies the namespaces of the entities referenced by this schema.</p>"""
    created_date: "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the schema was originally created.</p>"""
    last_updated_date: (
        "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    )
    """<p>The date and time that the schema was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutSchemaOutput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    import aws_sdk_verifiedpermissions.types.namespace_list

    out["namespaces"] = (
        aws_sdk_verifiedpermissions.types.namespace_list.serialize_aws_json_1_0(
            value["namespaces"]
        )
    )
    import aws_sdk_verifiedpermissions.types.timestamp_format

    out["createdDate"] = (
        aws_sdk_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    import aws_sdk_verifiedpermissions.types.timestamp_format

    out["lastUpdatedDate"] = (
        aws_sdk_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["last_updated_date"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutSchemaOutput:
    out: PutSchemaOutput = {}  # type: ignore[typeddict-item]
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("PutSchemaOutput.policy_store_id required")
    if "namespaces" in data:
        import aws_sdk_verifiedpermissions.types.namespace_list

        out["namespaces"] = (
            aws_sdk_verifiedpermissions.types.namespace_list.deserialize_aws_json_1_0(
                data["namespaces"]
            )
        )
    else:
        raise DeserializationError("PutSchemaOutput.namespaces required")
    if "createdDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("PutSchemaOutput.created_date required")
    if "lastUpdatedDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError("PutSchemaOutput.last_updated_date required")
    return out
