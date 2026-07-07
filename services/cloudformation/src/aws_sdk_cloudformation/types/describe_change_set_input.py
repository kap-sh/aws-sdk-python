"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeChangeSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.change_set_name_or_id
    import aws_sdk_cloudformation.types.include_property_values
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.stack_name_or_id


class DescribeChangeSetInput(TypedDict, closed=True):
    change_set_name: NotRequired[
        "aws_sdk_cloudformation.types.change_set_name_or_id.ChangeSetNameOrId"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the change set that you want to describe.</p>"""
    stack_name: NotRequired[
        "aws_sdk_cloudformation.types.stack_name_or_id.StackNameOrId"
    ]
    """<p>If you specified the name of a change set, specify the stack name or ID (ARN) of the change set you want to describe.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    include_property_values: NotRequired[
        "aws_sdk_cloudformation.types.include_property_values.IncludePropertyValues"
    ]
    """<p>If <code>true</code>, the returned changes include detailed changes in the property values.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeChangeSetInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "change_set_name" in value:
        pairs.append((f"{prefix}.ChangeSetName", str(value["change_set_name"])))
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "include_property_values" in value:
        pairs.append(
            (
                f"{prefix}.IncludePropertyValues",
                "true" if value["include_property_values"] else "false",
            )
        )


def deserialize_query(el: Element) -> DescribeChangeSetInput:
    out: DescribeChangeSetInput = {}  # type: ignore[typeddict-item]
    child_change_set_name = el.find("ChangeSetName")
    if child_change_set_name is not None:
        out["change_set_name"] = str(child_change_set_name.text or "")
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_include_property_values = el.find("IncludePropertyValues")
    if child_include_property_values is not None:
        out["include_property_values"] = (
            child_include_property_values.text or ""
        ).lower() == "true"
    return out
