"""Generated from Smithy shape ``com.amazonaws.ec2#PayerResponsibilityEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.payer_responsibility_scope
    import capo_ec2.types.payer_responsibility_type


class PayerResponsibilityEntry(TypedDict, closed=True):
    scope: NotRequired[
        "capo_ec2.types.payer_responsibility_scope.PayerResponsibilityScope"
    ]
    """<p>The scope of usage/charges.</p>"""
    payer_responsibility_type: NotRequired[
        "capo_ec2.types.payer_responsibility_type.PayerResponsibilityType"
    ]
    """<p>The Amazon Web Services account to which the usage is charged.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PayerResponsibilityEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "scope" in value:
        import capo_ec2.types.payer_responsibility_scope

        capo_ec2.types.payer_responsibility_scope.serialize_ec2_query(
            value["scope"], pairs, f"{key_prefix}Scope"
        )
    if "payer_responsibility_type" in value:
        import capo_ec2.types.payer_responsibility_type

        capo_ec2.types.payer_responsibility_type.serialize_ec2_query(
            value["payer_responsibility_type"],
            pairs,
            f"{key_prefix}PayerResponsibilityType",
        )


def deserialize_ec2_query(el: Element) -> PayerResponsibilityEntry:
    out: PayerResponsibilityEntry = {}  # type: ignore[typeddict-item]
    child_scope = el.find("scope")
    if child_scope is not None:
        import capo_ec2.types.payer_responsibility_scope

        out["scope"] = capo_ec2.types.payer_responsibility_scope.deserialize_ec2_query(
            child_scope
        )
    child_payer_responsibility_type = el.find("payerResponsibilityType")
    if child_payer_responsibility_type is not None:
        import capo_ec2.types.payer_responsibility_type

        out["payer_responsibility_type"] = (
            capo_ec2.types.payer_responsibility_type.deserialize_ec2_query(
                child_payer_responsibility_type
            )
        )
    return out
