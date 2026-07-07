"""Generated from Smithy shape ``com.amazonaws.cloudformation#RollbackStackInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.client_request_token
    import aws_sdk_cloudformation.types.retain_except_on_create
    import aws_sdk_cloudformation.types.role_arn
    import aws_sdk_cloudformation.types.stack_name_or_id


class RollbackStackInput(TypedDict, closed=True):
    stack_name: NotRequired[
        "aws_sdk_cloudformation.types.stack_name_or_id.StackNameOrId"
    ]
    """<p>The name that's associated with the stack.</p>"""
    role_arn: NotRequired["aws_sdk_cloudformation.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to rollback the stack.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique identifier for this <code>RollbackStack</code> request.</p>"""
    retain_except_on_create: NotRequired[
        "aws_sdk_cloudformation.types.retain_except_on_create.RetainExceptOnCreate"
    ]
    """<p>When set to <code>true</code>, newly created resources are deleted when the operation rolls back. This includes newly created resources marked with a deletion policy of <code>Retain</code>.</p> <p>Default: <code>false</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RollbackStackInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))
    if "role_arn" in value:
        pairs.append((f"{prefix}.RoleARN", str(value["role_arn"])))
    if "client_request_token" in value:
        pairs.append(
            (f"{prefix}.ClientRequestToken", str(value["client_request_token"]))
        )
    if "retain_except_on_create" in value:
        pairs.append(
            (
                f"{prefix}.RetainExceptOnCreate",
                "true" if value["retain_except_on_create"] else "false",
            )
        )


def deserialize_query(el: Element) -> RollbackStackInput:
    out: RollbackStackInput = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_role_arn = el.find("RoleARN")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    child_client_request_token = el.find("ClientRequestToken")
    if child_client_request_token is not None:
        out["client_request_token"] = str(child_client_request_token.text or "")
    child_retain_except_on_create = el.find("RetainExceptOnCreate")
    if child_retain_except_on_create is not None:
        out["retain_except_on_create"] = (
            child_retain_except_on_create.text or ""
        ).lower() == "true"
    return out
