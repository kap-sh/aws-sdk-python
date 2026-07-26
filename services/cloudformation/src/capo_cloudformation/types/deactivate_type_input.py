"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeactivateTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.private_type_arn
    import capo_cloudformation.types.third_party_type
    import capo_cloudformation.types.type_name


class DeactivateTypeInput(TypedDict, closed=True):
    type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>The type name of the extension in this account and Region. If you specified a type name alias when enabling the extension, use the type name alias.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>"""
    type: NotRequired["capo_cloudformation.types.third_party_type.ThirdPartyType"]
    """<p>The extension type.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>"""
    arn: NotRequired["capo_cloudformation.types.private_type_arn.PrivateTypeArn"]
    """<p>The Amazon Resource Name (ARN) for the extension in this account and Region.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeactivateTypeInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "type_name" in value:
        pairs.append((f"{prefix}.TypeName", str(value["type_name"])))
    if "type" in value:
        import capo_cloudformation.types.third_party_type

        capo_cloudformation.types.third_party_type.serialize_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "arn" in value:
        pairs.append((f"{prefix}.Arn", str(value["arn"])))


def deserialize_query(el: Element) -> DeactivateTypeInput:
    out: DeactivateTypeInput = {}  # type: ignore[typeddict-item]
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudformation.types.third_party_type

        out["type"] = capo_cloudformation.types.third_party_type.deserialize_query(
            child_type
        )
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
