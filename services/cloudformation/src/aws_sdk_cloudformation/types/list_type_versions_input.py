"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListTypeVersionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.deprecated_status
    import aws_sdk_cloudformation.types.max_results
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.publisher_id
    import aws_sdk_cloudformation.types.registry_type
    import aws_sdk_cloudformation.types.type_arn
    import aws_sdk_cloudformation.types.type_name


class ListTypeVersionsInput(TypedDict):
    type: NotRequired["aws_sdk_cloudformation.types.registry_type.RegistryType"]
    """<p>The kind of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>"""
    type_name: NotRequired["aws_sdk_cloudformation.types.type_name.TypeName"]
    """<p>The name of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>"""
    arn: NotRequired["aws_sdk_cloudformation.types.type_arn.TypeArn"]
    """<p>The Amazon Resource Name (ARN) of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>"""
    max_results: NotRequired["aws_sdk_cloudformation.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    deprecated_status: NotRequired[
        "aws_sdk_cloudformation.types.deprecated_status.DeprecatedStatus"
    ]
    """<p>The deprecation status of the extension versions that you want to get summary information about.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension version is registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension version has been deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul> <p>The default is <code>LIVE</code>.</p>"""
    publisher_id: NotRequired["aws_sdk_cloudformation.types.publisher_id.PublisherId"]
    """<p>The publisher ID of the extension publisher.</p> <p>Extensions published by Amazon aren't assigned a publisher ID.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTypeVersionsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "type" in value:
        import aws_sdk_cloudformation.types.registry_type

        aws_sdk_cloudformation.types.registry_type.serialize_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "type_name" in value:
        pairs.append((f"{prefix}.TypeName", str(value["type_name"])))
    if "arn" in value:
        pairs.append((f"{prefix}.Arn", str(value["arn"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "deprecated_status" in value:
        import aws_sdk_cloudformation.types.deprecated_status

        aws_sdk_cloudformation.types.deprecated_status.serialize_query(
            value["deprecated_status"], pairs, f"{prefix}.DeprecatedStatus"
        )
    if "publisher_id" in value:
        pairs.append((f"{prefix}.PublisherId", str(value["publisher_id"])))


def deserialize_query(el: Element) -> ListTypeVersionsInput:
    out: ListTypeVersionsInput = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_cloudformation.types.registry_type

        out["type"] = aws_sdk_cloudformation.types.registry_type.deserialize_query(
            child_type
        )
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_deprecated_status = el.find("DeprecatedStatus")
    if child_deprecated_status is not None:
        import aws_sdk_cloudformation.types.deprecated_status

        out["deprecated_status"] = (
            aws_sdk_cloudformation.types.deprecated_status.deserialize_query(
                child_deprecated_status
            )
        )
    child_publisher_id = el.find("PublisherId")
    if child_publisher_id is not None:
        out["publisher_id"] = str(child_publisher_id.text or "")
    return out
