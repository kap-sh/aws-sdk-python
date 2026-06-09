"""Generated from Smithy shape ``com.amazonaws.ec2#ImageCriterionRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_criterion_request

ImageCriterionRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.image_criterion_request.ImageCriterionRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageCriterionRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.image_criterion_request

        aws_sdk_ec2.types.image_criterion_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ImageCriterionRequestList:
    import aws_sdk_ec2.types.image_criterion_request

    out: ImageCriterionRequestList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.image_criterion_request.deserialize_ec2_query(child)
        )
    return out
