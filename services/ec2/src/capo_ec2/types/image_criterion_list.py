"""Generated from Smithy shape ``com.amazonaws.ec2#ImageCriterionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_criterion

ImageCriterionList: TypeAlias = list["capo_ec2.types.image_criterion.ImageCriterion"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageCriterionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.image_criterion

        capo_ec2.types.image_criterion.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> ImageCriterionList:
    import capo_ec2.types.image_criterion

    out: ImageCriterionList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.image_criterion.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ImageCriterionList:
    import capo_ec2.types.image_criterion

    out: ImageCriterionList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.image_criterion.deserialize_ec2_query(child))
    return out
