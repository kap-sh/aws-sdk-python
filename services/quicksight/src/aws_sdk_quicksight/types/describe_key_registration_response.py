"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeKeyRegistrationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.key_registration
    import aws_sdk_quicksight.types.non_empty_string
    import aws_sdk_quicksight.types.q_data_key
    import aws_sdk_quicksight.types.status_code


class DescribeKeyRegistrationResponse(TypedDict):
    aws_account_id: NotRequired["aws_sdk_quicksight.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the Amazon Web Services account that contains the customer managed key registration specified in the request.</p>"""
    key_registration: NotRequired[
        "aws_sdk_quicksight.types.key_registration.KeyRegistration"
    ]
    """<p>A list of <code>RegisteredCustomerManagedKey</code> objects in a Quick Sight account.</p>"""
    q_data_key: NotRequired["aws_sdk_quicksight.types.q_data_key.QDataKey"]
    """<p>A list of <code>QDataKey</code> objects in a Quick Sight account.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeKeyRegistrationResponse) -> dict:
    out: dict = {}
    if "aws_account_id" in value:
        out["AwsAccountId"] = value["aws_account_id"]
    if "key_registration" in value:
        import aws_sdk_quicksight.types.key_registration

        out["KeyRegistration"] = (
            aws_sdk_quicksight.types.key_registration.serialize_json(
                value["key_registration"]
            )
        )
    if "q_data_key" in value:
        import aws_sdk_quicksight.types.q_data_key

        out["QDataKey"] = aws_sdk_quicksight.types.q_data_key.serialize_json(
            value["q_data_key"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    out["Status"] = value.get("status", 0)
    return out


def deserialize_json(data: dict) -> DescribeKeyRegistrationResponse:
    out: DescribeKeyRegistrationResponse = {}  # type: ignore[typeddict-item]
    if "AwsAccountId" in data:
        out["aws_account_id"] = data["AwsAccountId"]
    if "KeyRegistration" in data:
        import aws_sdk_quicksight.types.key_registration

        out["key_registration"] = (
            aws_sdk_quicksight.types.key_registration.deserialize_json(
                data["KeyRegistration"]
            )
        )
    if "QDataKey" in data:
        import aws_sdk_quicksight.types.q_data_key

        out["q_data_key"] = aws_sdk_quicksight.types.q_data_key.deserialize_json(
            data["QDataKey"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        out["status"] = 0
    return out
