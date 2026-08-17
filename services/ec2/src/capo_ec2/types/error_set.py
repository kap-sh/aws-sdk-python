"""Generated from Smithy shape ``com.amazonaws.ec2#ErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.validation_error

ErrorSet: TypeAlias = list["capo_ec2.types.validation_error.ValidationError"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ErrorSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.validation_error

        capo_ec2.types.validation_error.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ErrorSet:
    import capo_ec2.types.validation_error

    out: ErrorSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.validation_error.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ErrorSet:
    import capo_ec2.types.validation_error

    out: ErrorSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.validation_error.deserialize_ec2_query(child))
    return out
