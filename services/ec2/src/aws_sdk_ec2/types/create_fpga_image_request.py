"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFpgaImageRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.storage_location
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateFpgaImageRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    input_storage_location: NotRequired[
        "aws_sdk_ec2.types.storage_location.StorageLocation"
    ]
    """<p>The location of the encrypted design checkpoint in Amazon S3. The input must be a tarball.</p>"""
    logs_storage_location: NotRequired[
        "aws_sdk_ec2.types.storage_location.StorageLocation"
    ]
    """<p>The location in Amazon S3 for the output logs.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the AFI.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A name for the AFI.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring Idempotency</a>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the FPGA image during creation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateFpgaImageRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "input_storage_location" in value:
        import aws_sdk_ec2.types.storage_location

        aws_sdk_ec2.types.storage_location.serialize_ec2_query(
            value["input_storage_location"], pairs, f"{prefix}.InputStorageLocation"
        )
    if "logs_storage_location" in value:
        import aws_sdk_ec2.types.storage_location

        aws_sdk_ec2.types.storage_location.serialize_ec2_query(
            value["logs_storage_location"], pairs, f"{prefix}.LogsStorageLocation"
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )


def deserialize_ec2_query(el: Element) -> CreateFpgaImageRequest:
    out: CreateFpgaImageRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_input_storage_location = el.find("InputStorageLocation")
    if child_input_storage_location is not None:
        import aws_sdk_ec2.types.storage_location

        out["input_storage_location"] = (
            aws_sdk_ec2.types.storage_location.deserialize_ec2_query(
                child_input_storage_location
            )
        )
    child_logs_storage_location = el.find("LogsStorageLocation")
    if child_logs_storage_location is not None:
        import aws_sdk_ec2.types.storage_location

        out["logs_storage_location"] = (
            aws_sdk_ec2.types.storage_location.deserialize_ec2_query(
                child_logs_storage_location
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    return out
