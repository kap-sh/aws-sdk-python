"""Generated from Smithy shape ``com.amazonaws.ec2#ImageMetadata``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.image_state
    import aws_sdk_ec2.types.string


class ImageMetadata(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the AMI.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the AMI.</p>"""
    state: NotRequired["aws_sdk_ec2.types.image_state.ImageState"]
    """<p>The current state of the AMI. If the state is <code>available</code>, the AMI is successfully registered and can be used to launch an instance.</p>"""
    image_owner_alias: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The alias of the AMI owner.</p> <p>Valid values: <code>amazon</code> | <code>aws-backup-vault</code> | <code>aws-marketplace</code> </p>"""
    creation_date: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The date and time the AMI was created.</p>"""
    deprecation_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The deprecation date and time of the AMI, in UTC, in the following format: <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z.</p>"""
    image_allowed: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, the AMI satisfies the criteria for Allowed AMIs and can be discovered and used in the account. If <code>false</code>, the AMI can't be discovered or used in the account.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html\">Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs</a> in <i>Amazon EC2 User Guide</i>.</p>"""
    is_public: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the AMI has public launch permissions. A value of <code>true</code> means this AMI has public launch permissions, while <code>false</code> means it has only implicit (AMI owner) or explicit (shared with your account) launch permissions.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageMetadata, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "owner_id" in value:
        pairs.append((f"{prefix}.ImageOwnerId", str(value["owner_id"])))
    if "state" in value:
        import aws_sdk_ec2.types.image_state

        aws_sdk_ec2.types.image_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.ImageState"
        )
    if "image_owner_alias" in value:
        pairs.append((f"{prefix}.ImageOwnerAlias", str(value["image_owner_alias"])))
    if "creation_date" in value:
        pairs.append((f"{prefix}.CreationDate", str(value["creation_date"])))
    if "deprecation_time" in value:
        pairs.append((f"{prefix}.DeprecationTime", str(value["deprecation_time"])))
    if "image_allowed" in value:
        pairs.append(
            (f"{prefix}.ImageAllowed", "true" if value["image_allowed"] else "false")
        )
    if "is_public" in value:
        pairs.append((f"{prefix}.IsPublic", "true" if value["is_public"] else "false"))


def deserialize_ec2_query(el: Element) -> ImageMetadata:
    out: ImageMetadata = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_owner_id = el.find("ImageOwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_state = el.find("ImageState")
    if child_state is not None:
        import aws_sdk_ec2.types.image_state

        out["state"] = aws_sdk_ec2.types.image_state.deserialize_ec2_query(child_state)
    child_image_owner_alias = el.find("ImageOwnerAlias")
    if child_image_owner_alias is not None:
        out["image_owner_alias"] = str(child_image_owner_alias.text or "")
    child_creation_date = el.find("CreationDate")
    if child_creation_date is not None:
        out["creation_date"] = str(child_creation_date.text or "")
    child_deprecation_time = el.find("DeprecationTime")
    if child_deprecation_time is not None:
        out["deprecation_time"] = str(child_deprecation_time.text or "")
    child_image_allowed = el.find("ImageAllowed")
    if child_image_allowed is not None:
        out["image_allowed"] = (child_image_allowed.text or "").lower() == "true"
    child_is_public = el.find("IsPublic")
    if child_is_public is not None:
        out["is_public"] = (child_is_public.text or "").lower() == "true"
    return out
