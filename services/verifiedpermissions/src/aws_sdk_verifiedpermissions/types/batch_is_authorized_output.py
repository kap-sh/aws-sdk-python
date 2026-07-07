"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchIsAuthorizedOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.batch_is_authorized_output_list


class BatchIsAuthorizedOutput(TypedDict, closed=True):
    results: "aws_sdk_verifiedpermissions.types.batch_is_authorized_output_list.BatchIsAuthorizedOutputList"
    """<p>A series of <code>Allow</code> or <code>Deny</code> decisions for each request, and the policies that produced them. These results are returned in the order they were requested.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchIsAuthorizedOutput) -> dict:
    out: dict = {}
    import aws_sdk_verifiedpermissions.types.batch_is_authorized_output_list

    out["results"] = (
        aws_sdk_verifiedpermissions.types.batch_is_authorized_output_list.serialize_aws_json_1_0(
            value["results"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchIsAuthorizedOutput:
    out: BatchIsAuthorizedOutput = {}  # type: ignore[typeddict-item]
    if "results" in data:
        import aws_sdk_verifiedpermissions.types.batch_is_authorized_output_list

        out["results"] = (
            aws_sdk_verifiedpermissions.types.batch_is_authorized_output_list.deserialize_aws_json_1_0(
                data["results"]
            )
        )
    else:
        raise DeserializationError("BatchIsAuthorizedOutput.results required")
    return out
