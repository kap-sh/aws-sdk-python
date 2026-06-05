"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFpgaImagesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_fpga_images_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.fpga_image_id_list
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.owner_string_list


class DescribeFpgaImagesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    fpga_image_ids: NotRequired["aws_sdk_ec2.types.fpga_image_id_list.FpgaImageIdList"]
    """<p>The AFI IDs.</p>"""
    owners: NotRequired["aws_sdk_ec2.types.owner_string_list.OwnerStringList"]
    """<p>Filters the AFI by owner. Specify an Amazon Web Services account ID, <code>self</code> (owner is the sender of the request), or an Amazon Web Services owner alias (valid values are <code>amazon</code> | <code>aws-marketplace</code>).</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>create-time</code> - The creation time of the AFI.</p> </li> <li> <p> <code>fpga-image-id</code> - The FPGA image identifier (AFI ID).</p> </li> <li> <p> <code>fpga-image-global-id</code> - The global FPGA image identifier (AGFI ID).</p> </li> <li> <p> <code>name</code> - The name of the AFI.</p> </li> <li> <p> <code>owner-id</code> - The Amazon Web Services account ID of the AFI owner.</p> </li> <li> <p> <code>product-code</code> - The product code.</p> </li> <li> <p> <code>shell-version</code> - The version of the Amazon Web Services Shell that was used to create the bitstream.</p> </li> <li> <p> <code>state</code> - The state of the AFI (<code>pending</code> | <code>failed</code> | <code>available</code> | <code>unavailable</code>).</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>update-time</code> - The time of the most recent update.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_fpga_images_max_results.DescribeFpgaImagesMaxResults"
    ]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFpgaImagesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "fpga_image_ids" in value:
        import aws_sdk_ec2.types.fpga_image_id_list

        aws_sdk_ec2.types.fpga_image_id_list.serialize_ec2_query(
            value["fpga_image_ids"], pairs, f"{prefix}.FpgaImageIds"
        )
    if "owners" in value:
        import aws_sdk_ec2.types.owner_string_list

        aws_sdk_ec2.types.owner_string_list.serialize_ec2_query(
            value["owners"], pairs, f"{prefix}.Owners"
        )
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> DescribeFpgaImagesRequest:
    out: DescribeFpgaImagesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("FpgaImageIds") is not None:
        import aws_sdk_ec2.types.fpga_image_id_list

        out["fpga_image_ids"] = (
            aws_sdk_ec2.types.fpga_image_id_list.deserialize_ec2_query(
                el, "FpgaImageIds"
            )
        )
    if el.find("Owners") is not None:
        import aws_sdk_ec2.types.owner_string_list

        out["owners"] = aws_sdk_ec2.types.owner_string_list.deserialize_ec2_query(
            el, "Owners"
        )
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
