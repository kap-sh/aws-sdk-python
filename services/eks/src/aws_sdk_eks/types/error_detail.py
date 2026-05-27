"""Generated from Smithy shape ``com.amazonaws.eks#ErrorDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.error_code
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list


class ErrorDetail(TypedDict):
    error_code: NotRequired["aws_sdk_eks.types.error_code.ErrorCode"]
    """<p>A brief description of the error. </p> <ul> <li> <p> <b>SubnetNotFound</b>: We couldn't find one of the subnets associated with the cluster.</p> </li> <li> <p> <b>SecurityGroupNotFound</b>: We couldn't find one of the security groups associated with the cluster.</p> </li> <li> <p> <b>EniLimitReached</b>: You have reached the elastic network interface limit for your account.</p> </li> <li> <p> <b>IpNotAvailable</b>: A subnet associated with the cluster doesn't have any available IP addresses.</p> </li> <li> <p> <b>AccessDenied</b>: You don't have permissions to perform the specified operation.</p> </li> <li> <p> <b>OperationNotPermitted</b>: The service role associated with the cluster doesn't have the required access permissions for Amazon EKS.</p> </li> <li> <p> <b>VpcIdNotFound</b>: We couldn't find the VPC associated with the cluster.</p> </li> </ul>"""
    error_message: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>A more complete description of the error.</p>"""
    resource_ids: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>An optional field that contains the resource IDs associated with the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetail) -> dict:
    out: dict = {}
    if "error_code" in value:
        import aws_sdk_eks.types.error_code

        out["errorCode"] = aws_sdk_eks.types.error_code.serialize_json(
            value["error_code"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "resource_ids" in value:
        import aws_sdk_eks.types.string_list

        out["resourceIds"] = aws_sdk_eks.types.string_list.serialize_json(
            value["resource_ids"]
        )
    return out


def deserialize_json(data: dict) -> ErrorDetail:
    out: ErrorDetail = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        import aws_sdk_eks.types.error_code

        out["error_code"] = aws_sdk_eks.types.error_code.deserialize_json(
            data["errorCode"]
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "resourceIds" in data:
        import aws_sdk_eks.types.string_list

        out["resource_ids"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["resourceIds"]
        )
    return out
