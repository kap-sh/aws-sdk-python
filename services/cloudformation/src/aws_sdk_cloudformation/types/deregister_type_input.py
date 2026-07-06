"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeregisterTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.private_type_arn
    import aws_sdk_cloudformation.types.registry_type
    import aws_sdk_cloudformation.types.type_name
    import aws_sdk_cloudformation.types.type_version_id


class DeregisterTypeInput(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_cloudformation.types.private_type_arn.PrivateTypeArn"]
    """<p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>"""
    type: NotRequired["aws_sdk_cloudformation.types.registry_type.RegistryType"]
    """<p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>"""
    type_name: NotRequired["aws_sdk_cloudformation.types.type_name.TypeName"]
    """<p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>"""
    version_id: NotRequired[
        "aws_sdk_cloudformation.types.type_version_id.TypeVersionId"
    ]
    """<p>The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeregisterTypeInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "arn" in value:
        pairs.append((f"{prefix}.Arn", str(value["arn"])))
    if "type" in value:
        import aws_sdk_cloudformation.types.registry_type

        aws_sdk_cloudformation.types.registry_type.serialize_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "type_name" in value:
        pairs.append((f"{prefix}.TypeName", str(value["type_name"])))
    if "version_id" in value:
        pairs.append((f"{prefix}.VersionId", str(value["version_id"])))


def deserialize_query(el: Element) -> DeregisterTypeInput:
    out: DeregisterTypeInput = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_cloudformation.types.registry_type

        out["type"] = aws_sdk_cloudformation.types.registry_type.deserialize_query(
            child_type
        )
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_version_id = el.find("VersionId")
    if child_version_id is not None:
        out["version_id"] = str(child_version_id.text or "")
    return out
