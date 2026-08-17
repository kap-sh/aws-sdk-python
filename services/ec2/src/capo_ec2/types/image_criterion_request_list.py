"""Generated from Smithy shape ``com.amazonaws.ec2#ImageCriterionRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_criterion_request

ImageCriterionRequestList: TypeAlias = list[
    "capo_ec2.types.image_criterion_request.ImageCriterionRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageCriterionRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.image_criterion_request

        capo_ec2.types.image_criterion_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ImageCriterionRequestList:
    import capo_ec2.types.image_criterion_request

    out: ImageCriterionRequestList = []
    for child in el.findall("ImageCriterion"):
        out.append(capo_ec2.types.image_criterion_request.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ImageCriterionRequestList:
    import capo_ec2.types.image_criterion_request

    out: ImageCriterionRequestList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.image_criterion_request.deserialize_ec2_query(child))
    return out
