"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.public_version_number
    import capo_cloudformation.types.publisher_id
    import capo_cloudformation.types.registry_type
    import capo_cloudformation.types.type_arn
    import capo_cloudformation.types.type_name
    import capo_cloudformation.types.type_version_id


class DescribeTypeInput(TypedDict, closed=True):
    type: NotRequired["capo_cloudformation.types.registry_type.RegistryType"]
    """<p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>"""
    type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>"""
    arn: NotRequired["capo_cloudformation.types.type_arn.TypeArn"]
    """<p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>"""
    version_id: NotRequired["capo_cloudformation.types.type_version_id.TypeVersionId"]
    """<p>The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.</p> <p>If you specify a <code>VersionId</code>, <code>DescribeType</code> returns information about that specific extension version. Otherwise, it returns information about the default extension version.</p>"""
    publisher_id: NotRequired["capo_cloudformation.types.publisher_id.PublisherId"]
    """<p>The publisher ID of the extension publisher.</p> <p>Extensions provided by Amazon Web Services are not assigned a publisher ID.</p>"""
    public_version_number: NotRequired[
        "capo_cloudformation.types.public_version_number.PublicVersionNumber"
    ]
    """<p>The version number of a public third-party extension.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTypeInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "type" in value:
        import capo_cloudformation.types.registry_type

        capo_cloudformation.types.registry_type.serialize_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "type_name" in value:
        pairs.append((f"{prefix}.TypeName", str(value["type_name"])))
    if "arn" in value:
        pairs.append((f"{prefix}.Arn", str(value["arn"])))
    if "version_id" in value:
        pairs.append((f"{prefix}.VersionId", str(value["version_id"])))
    if "publisher_id" in value:
        pairs.append((f"{prefix}.PublisherId", str(value["publisher_id"])))
    if "public_version_number" in value:
        pairs.append(
            (f"{prefix}.PublicVersionNumber", str(value["public_version_number"]))
        )


def deserialize_query(el: Element) -> DescribeTypeInput:
    out: DescribeTypeInput = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudformation.types.registry_type

        out["type"] = capo_cloudformation.types.registry_type.deserialize_query(
            child_type
        )
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_version_id = el.find("VersionId")
    if child_version_id is not None:
        out["version_id"] = str(child_version_id.text or "")
    child_publisher_id = el.find("PublisherId")
    if child_publisher_id is not None:
        out["publisher_id"] = str(child_publisher_id.text or "")
    child_public_version_number = el.find("PublicVersionNumber")
    if child_public_version_number is not None:
        out["public_version_number"] = str(child_public_version_number.text or "")
    return out
