"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.client_request_token
    import aws_sdk_iot_wireless.types.description
    import aws_sdk_iot_wireless.types.destination_name
    import aws_sdk_iot_wireless.types.expression
    import aws_sdk_iot_wireless.types.expression_type
    import aws_sdk_iot_wireless.types.role_arn
    import aws_sdk_iot_wireless.types.tag_list


class CreateDestinationRequest(TypedDict):
    name: "aws_sdk_iot_wireless.types.destination_name.DestinationName"
    """<p>The name of the new resource.</p>"""
    expression_type: "aws_sdk_iot_wireless.types.expression_type.ExpressionType"
    """<p>The type of value in <code>Expression</code>.</p>"""
    expression: "aws_sdk_iot_wireless.types.expression.Expression"
    """<p>The rule name or topic rule to send messages to.</p>"""
    description: NotRequired["aws_sdk_iot_wireless.types.description.Description"]
    """<p>The description of the new resource.</p>"""
    role_arn: "aws_sdk_iot_wireless.types.role_arn.RoleArn"
    """<p>The ARN of the IAM Role that authorizes the destination.</p>"""
    tags: NotRequired["aws_sdk_iot_wireless.types.tag_list.TagList"]
    """<p>The tags to attach to the new destination. Tags are metadata that you can use to manage a resource.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
    ]
    r"""<p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDestinationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_iot_wireless.types.expression_type

    out["ExpressionType"] = aws_sdk_iot_wireless.types.expression_type.serialize_json(
        value["expression_type"]
    )
    out["Expression"] = value["expression"]
    if "description" in value:
        out["Description"] = value["description"]
    out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_iot_wireless.types.tag_list

        out["Tags"] = aws_sdk_iot_wireless.types.tag_list.serialize_json(value["tags"])
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateDestinationRequest:
    out: CreateDestinationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDestinationRequest.name required")
    if "ExpressionType" in data:
        import aws_sdk_iot_wireless.types.expression_type

        out["expression_type"] = (
            aws_sdk_iot_wireless.types.expression_type.deserialize_json(
                data["ExpressionType"]
            )
        )
    else:
        raise DeserializationError("CreateDestinationRequest.expression_type required")
    if "Expression" in data:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError("CreateDestinationRequest.expression required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("CreateDestinationRequest.role_arn required")
    if "Tags" in data:
        import aws_sdk_iot_wireless.types.tag_list

        out["tags"] = aws_sdk_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
