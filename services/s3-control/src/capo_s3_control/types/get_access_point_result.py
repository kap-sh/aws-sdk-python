"""Generated from Smithy shape ``com.amazonaws.s3control#GetAccessPointResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.access_point_bucket_name
    import capo_s3_control.types.access_point_name
    import capo_s3_control.types.account_id
    import capo_s3_control.types.alias
    import capo_s3_control.types.creation_date
    import capo_s3_control.types.data_source_id
    import capo_s3_control.types.data_source_type
    import capo_s3_control.types.endpoints
    import capo_s3_control.types.network_origin
    import capo_s3_control.types.public_access_block_configuration
    import capo_s3_control.types.s3_access_point_arn
    import capo_s3_control.types.vpc_configuration


class GetAccessPointResult(TypedDict, closed=True):
    name: NotRequired["capo_s3_control.types.access_point_name.AccessPointName"]
    """<p>The name of the specified access point.</p>"""
    bucket: NotRequired[
        "capo_s3_control.types.access_point_bucket_name.AccessPointBucketName"
    ]
    """<p>The name of the bucket associated with the specified access point.</p>"""
    network_origin: NotRequired["capo_s3_control.types.network_origin.NetworkOrigin"]
    """<p>Indicates whether this access point allows access from the public internet. If <code>VpcConfiguration</code> is specified for this access point, then <code>NetworkOrigin</code> is <code>VPC</code>, and the access point doesn't allow access from the public internet. Otherwise, <code>NetworkOrigin</code> is <code>Internet</code>, and the access point allows access from the public internet, subject to the access point and bucket access policies.</p> <p>This will always be true for an Amazon S3 on Outposts access point</p>"""
    vpc_configuration: NotRequired[
        "capo_s3_control.types.vpc_configuration.VpcConfiguration"
    ]
    """<p>Contains the virtual private cloud (VPC) configuration for the specified access point.</p> <note> <p>This element is empty if this access point is an Amazon S3 on Outposts access point that is used by other Amazon Web Services services.</p> </note>"""
    public_access_block_configuration: NotRequired[
        "capo_s3_control.types.public_access_block_configuration.PublicAccessBlockConfiguration"
    ]
    creation_date: NotRequired["capo_s3_control.types.creation_date.CreationDate"]
    """<p>The date and time when the specified access point was created.</p>"""
    alias: NotRequired["capo_s3_control.types.alias.Alias"]
    """<p>The name or alias of the access point.</p>"""
    access_point_arn: NotRequired[
        "capo_s3_control.types.s3_access_point_arn.S3AccessPointArn"
    ]
    """<p>The ARN of the access point.</p>"""
    endpoints: NotRequired["capo_s3_control.types.endpoints.Endpoints"]
    """<p>The VPC endpoint for the access point.</p>"""
    bucket_account_id: NotRequired["capo_s3_control.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID associated with the S3 bucket associated with this access point.</p>"""
    data_source_id: NotRequired["capo_s3_control.types.data_source_id.DataSourceId"]
    """<p>The unique identifier for the data source of the access point.</p>"""
    data_source_type: NotRequired[
        "capo_s3_control.types.data_source_type.DataSourceType"
    ]
    """<p>The type of the data source that the access point is attached to.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetAccessPointResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "name" in value:
        SubElement(el, "Name").text = str(value["name"])
    if "bucket" in value:
        SubElement(el, "Bucket").text = str(value["bucket"])
    if "network_origin" in value:
        import capo_s3_control.types.network_origin

        capo_s3_control.types.network_origin.serialize_xml(
            value["network_origin"], el, "NetworkOrigin"
        )
    if "vpc_configuration" in value:
        import capo_s3_control.types.vpc_configuration

        capo_s3_control.types.vpc_configuration.serialize_xml(
            value["vpc_configuration"], el, "VpcConfiguration"
        )
    if "public_access_block_configuration" in value:
        import capo_s3_control.types.public_access_block_configuration

        capo_s3_control.types.public_access_block_configuration.serialize_xml(
            value["public_access_block_configuration"],
            el,
            "PublicAccessBlockConfiguration",
        )
    if "creation_date" in value:
        import capo_s3_control.types.creation_date

        capo_s3_control.types.creation_date.serialize_xml(
            value["creation_date"], el, "CreationDate"
        )
    if "alias" in value:
        SubElement(el, "Alias").text = str(value["alias"])
    if "access_point_arn" in value:
        SubElement(el, "AccessPointArn").text = str(value["access_point_arn"])
    if "endpoints" in value:
        import capo_s3_control.types.endpoints

        capo_s3_control.types.endpoints.serialize_xml(
            value["endpoints"], el, "Endpoints"
        )
    if "bucket_account_id" in value:
        SubElement(el, "BucketAccountId").text = str(value["bucket_account_id"])
    if "data_source_id" in value:
        SubElement(el, "DataSourceId").text = str(value["data_source_id"])
    if "data_source_type" in value:
        SubElement(el, "DataSourceType").text = str(value["data_source_type"])


def deserialize_xml(el: Element) -> GetAccessPointResult:
    out: GetAccessPointResult = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_network_origin = el.find("NetworkOrigin")
    if child_network_origin is not None:
        import capo_s3_control.types.network_origin

        out["network_origin"] = capo_s3_control.types.network_origin.deserialize_xml(
            child_network_origin
        )
    child_vpc_configuration = el.find("VpcConfiguration")
    if child_vpc_configuration is not None:
        import capo_s3_control.types.vpc_configuration

        out["vpc_configuration"] = (
            capo_s3_control.types.vpc_configuration.deserialize_xml(
                child_vpc_configuration
            )
        )
    child_public_access_block_configuration = el.find("PublicAccessBlockConfiguration")
    if child_public_access_block_configuration is not None:
        import capo_s3_control.types.public_access_block_configuration

        out["public_access_block_configuration"] = (
            capo_s3_control.types.public_access_block_configuration.deserialize_xml(
                child_public_access_block_configuration
            )
        )
    child_creation_date = el.find("CreationDate")
    if child_creation_date is not None:
        import capo_s3_control.types.creation_date

        out["creation_date"] = capo_s3_control.types.creation_date.deserialize_xml(
            child_creation_date
        )
    child_alias = el.find("Alias")
    if child_alias is not None:
        out["alias"] = str(child_alias.text or "")
    child_access_point_arn = el.find("AccessPointArn")
    if child_access_point_arn is not None:
        out["access_point_arn"] = str(child_access_point_arn.text or "")
    child_endpoints = el.find("Endpoints")
    if child_endpoints is not None:
        import capo_s3_control.types.endpoints

        out["endpoints"] = capo_s3_control.types.endpoints.deserialize_xml(
            child_endpoints
        )
    child_bucket_account_id = el.find("BucketAccountId")
    if child_bucket_account_id is not None:
        out["bucket_account_id"] = str(child_bucket_account_id.text or "")
    child_data_source_id = el.find("DataSourceId")
    if child_data_source_id is not None:
        out["data_source_id"] = str(child_data_source_id.text or "")
    child_data_source_type = el.find("DataSourceType")
    if child_data_source_type is not None:
        out["data_source_type"] = str(child_data_source_type.text or "")
    return out
