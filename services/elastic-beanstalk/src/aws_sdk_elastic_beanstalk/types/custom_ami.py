"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#CustomAmi``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.image_id
    import aws_sdk_elastic_beanstalk.types.virtualization_type


class CustomAmi(TypedDict):
    virtualization_type: NotRequired[
        "aws_sdk_elastic_beanstalk.types.virtualization_type.VirtualizationType"
    ]
    """<p>The type of virtualization used to create the custom AMI.</p>"""
    image_id: NotRequired["aws_sdk_elastic_beanstalk.types.image_id.ImageId"]
    """<p>THe ID of the image used to create the custom AMI.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomAmi, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "virtualization_type" in value:
        pairs.append(
            (f"{prefix}.VirtualizationType", str(value["virtualization_type"]))
        )
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))


def deserialize_query(el: Element) -> CustomAmi:
    out: CustomAmi = {}  # type: ignore[typeddict-item]
    child_virtualization_type = el.find("VirtualizationType")
    if child_virtualization_type is not None:
        out["virtualization_type"] = str(child_virtualization_type.text or "")
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    return out
