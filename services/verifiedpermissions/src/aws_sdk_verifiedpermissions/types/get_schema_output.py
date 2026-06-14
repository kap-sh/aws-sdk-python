"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#GetSchemaOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.namespace_list
    import aws_sdk_verifiedpermissions.types.policy_store_id
    import aws_sdk_verifiedpermissions.types.schema_json
    import aws_sdk_verifiedpermissions.types.timestamp_format


class GetSchemaOutput(TypedDict):
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The ID of the policy store that contains the schema.</p>"""
    schema: "aws_sdk_verifiedpermissions.types.schema_json.SchemaJson"
    """<p>The body of the schema, written in Cedar schema JSON.</p>"""
    created_date: "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the schema was originally created.</p>"""
    last_updated_date: (
        "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    )
    """<p>The date and time that the schema was most recently updated.</p>"""
    namespaces: NotRequired[
        "aws_sdk_verifiedpermissions.types.namespace_list.NamespaceList"
    ]
    """<p>The namespaces of the entities referenced by this schema.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSchemaOutput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["schema"] = value["schema"]
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
    if "namespaces" in value:
        import aws_sdk_verifiedpermissions.types.namespace_list

        out["namespaces"] = (
            aws_sdk_verifiedpermissions.types.namespace_list.serialize_aws_json_1_0(
                value["namespaces"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSchemaOutput:
    out: GetSchemaOutput = {}  # type: ignore[typeddict-item]
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("GetSchemaOutput.policy_store_id required")
    if "schema" in data:
        out["schema"] = data["schema"]
    else:
        raise DeserializationError("GetSchemaOutput.schema required")
    if "createdDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("GetSchemaOutput.created_date required")
    if "lastUpdatedDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError("GetSchemaOutput.last_updated_date required")
    if "namespaces" in data:
        import aws_sdk_verifiedpermissions.types.namespace_list

        out["namespaces"] = (
            aws_sdk_verifiedpermissions.types.namespace_list.deserialize_aws_json_1_0(
                data["namespaces"]
            )
        )
    return out
