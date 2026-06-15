"""Generated from Smithy shape ``com.amazonaws.connect#BatchPutContactRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.contact_data_request_list
    import aws_sdk_connect.types.instance_id


class BatchPutContactRequest(TypedDict):
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_data_request_list: (
        "aws_sdk_connect.types.contact_data_request_list.ContactDataRequestList"
    )
    """<p>List of individual contact requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutContactRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    import aws_sdk_connect.types.contact_data_request_list

    out["ContactDataRequestList"] = (
        aws_sdk_connect.types.contact_data_request_list.serialize_json(
            value["contact_data_request_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchPutContactRequest:
    out: BatchPutContactRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "ContactDataRequestList" in data:
        import aws_sdk_connect.types.contact_data_request_list

        out["contact_data_request_list"] = (
            aws_sdk_connect.types.contact_data_request_list.deserialize_json(
                data["ContactDataRequestList"]
            )
        )
    else:
        raise DeserializationError(
            "BatchPutContactRequest.contact_data_request_list required"
        )
    return out
