"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchIsAuthorizedWithTokenOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.batch_is_authorized_with_token_output_list
    import aws_sdk_verifiedpermissions.types.entity_identifier


class BatchIsAuthorizedWithTokenOutput(TypedDict):
    principal: NotRequired[
        "aws_sdk_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>The identifier of the principal in the ID or access token.</p>"""
    results: "aws_sdk_verifiedpermissions.types.batch_is_authorized_with_token_output_list.BatchIsAuthorizedWithTokenOutputList"
    """<p>A series of <code>Allow</code> or <code>Deny</code> decisions for each request, and the policies that produced them. These results are returned in the order they were requested.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchIsAuthorizedWithTokenOutput) -> dict:
    out: dict = {}
    if "principal" in value:
        import aws_sdk_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            aws_sdk_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["principal"]
            )
        )
    import aws_sdk_verifiedpermissions.types.batch_is_authorized_with_token_output_list

    out["results"] = (
        aws_sdk_verifiedpermissions.types.batch_is_authorized_with_token_output_list.serialize_aws_json_1_0(
            value["results"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchIsAuthorizedWithTokenOutput:
    out: BatchIsAuthorizedWithTokenOutput = {}  # type: ignore[typeddict-item]
    if "principal" in data:
        import aws_sdk_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            aws_sdk_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["principal"]
            )
        )
    if "results" in data:
        import aws_sdk_verifiedpermissions.types.batch_is_authorized_with_token_output_list

        out["results"] = (
            aws_sdk_verifiedpermissions.types.batch_is_authorized_with_token_output_list.deserialize_aws_json_1_0(
                data["results"]
            )
        )
    else:
        raise DeserializationError("BatchIsAuthorizedWithTokenOutput.results required")
    return out
