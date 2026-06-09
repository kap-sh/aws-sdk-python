"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFastLaunchImagesSuccessSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_fast_launch_images_success_item

DescribeFastLaunchImagesSuccessSet: TypeAlias = list[
    "aws_sdk_ec2.types.describe_fast_launch_images_success_item.DescribeFastLaunchImagesSuccessItem"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFastLaunchImagesSuccessSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.describe_fast_launch_images_success_item

        aws_sdk_ec2.types.describe_fast_launch_images_success_item.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> DescribeFastLaunchImagesSuccessSet:
    import aws_sdk_ec2.types.describe_fast_launch_images_success_item

    out: DescribeFastLaunchImagesSuccessSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.describe_fast_launch_images_success_item.deserialize_ec2_query(
                child
            )
        )
    return out
