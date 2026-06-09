"""Generated from Smithy shape ``com.amazonaws.ec2#ExportTransitGatewayRoutesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ExportTransitGatewayRoutesResult(TypedDict):
    s3_location: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The URL of the exported file in Amazon S3. For example, s3://<i>bucket_name</i>/VPCTransitGateway/TransitGatewayRouteTables/<i>file_name</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportTransitGatewayRoutesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "s3_location" in value:
        pairs.append((f"{prefix}.S3Location", str(value["s3_location"])))


def deserialize_ec2_query(el: Element) -> ExportTransitGatewayRoutesResult:
    out: ExportTransitGatewayRoutesResult = {}  # type: ignore[typeddict-item]
    child_s3_location = el.find("S3Location")
    if child_s3_location is not None:
        out["s3_location"] = str(child_s3_location.text or "")
    return out
