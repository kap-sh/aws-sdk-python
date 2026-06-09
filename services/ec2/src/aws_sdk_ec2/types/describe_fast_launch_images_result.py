"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFastLaunchImagesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_fast_launch_images_success_set
    import aws_sdk_ec2.types.next_token


class DescribeFastLaunchImagesResult(TypedDict):
    fast_launch_images: NotRequired[
        "aws_sdk_ec2.types.describe_fast_launch_images_success_set.DescribeFastLaunchImagesSuccessSet"
    ]
    """<p>A collection of details about the fast-launch enabled Windows images that meet the requested criteria.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFastLaunchImagesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "fast_launch_images" in value:
        import aws_sdk_ec2.types.describe_fast_launch_images_success_set

        aws_sdk_ec2.types.describe_fast_launch_images_success_set.serialize_ec2_query(
            value["fast_launch_images"], pairs, f"{prefix}.FastLaunchImageSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeFastLaunchImagesResult:
    out: DescribeFastLaunchImagesResult = {}  # type: ignore[typeddict-item]
    if el.find("FastLaunchImageSet") is not None:
        import aws_sdk_ec2.types.describe_fast_launch_images_success_set

        out["fast_launch_images"] = (
            aws_sdk_ec2.types.describe_fast_launch_images_success_set.deserialize_ec2_query(
                el, "FastLaunchImageSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
