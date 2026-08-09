"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeKeyPairsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.key_name_string_list
    import capo_ec2.types.key_pair_id_string_list


class DescribeKeyPairsRequest(TypedDict, closed=True):
    key_names: NotRequired["capo_ec2.types.key_name_string_list.KeyNameStringList"]
    """<p>The key pair names.</p> <p>Default: Describes all of your key pairs.</p>"""
    key_pair_ids: NotRequired[
        "capo_ec2.types.key_pair_id_string_list.KeyPairIdStringList"
    ]
    """<p>The IDs of the key pairs.</p>"""
    include_public_key: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, the public key material is included in the response.</p> <p>Default: <code>false</code> </p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>key-pair-id</code> - The ID of the key pair.</p> </li> <li> <p> <code>fingerprint</code> - The fingerprint of the key pair.</p> </li> <li> <p> <code>key-name</code> - The name of the key pair.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeKeyPairsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "key_names" in value:
        import capo_ec2.types.key_name_string_list

        capo_ec2.types.key_name_string_list.serialize_ec2_query(
            value["key_names"], pairs, f"{key_prefix}KeyName"
        )
    if "key_pair_ids" in value:
        import capo_ec2.types.key_pair_id_string_list

        capo_ec2.types.key_pair_id_string_list.serialize_ec2_query(
            value["key_pair_ids"], pairs, f"{key_prefix}KeyPairId"
        )
    if "include_public_key" in value:
        pairs.append(
            (
                f"{key_prefix}IncludePublicKey",
                "true" if value["include_public_key"] else "false",
            )
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )


def deserialize_ec2_query(el: Element) -> DescribeKeyPairsRequest:
    out: DescribeKeyPairsRequest = {}  # type: ignore[typeddict-item]
    child_key_names = el.find("KeyName")
    if child_key_names is not None:
        import capo_ec2.types.key_name_string_list

        out["key_names"] = capo_ec2.types.key_name_string_list.deserialize_ec2_query(
            child_key_names
        )
    child_key_pair_ids = el.find("KeyPairId")
    if child_key_pair_ids is not None:
        import capo_ec2.types.key_pair_id_string_list

        out["key_pair_ids"] = (
            capo_ec2.types.key_pair_id_string_list.deserialize_ec2_query(
                child_key_pair_ids
            )
        )
    child_include_public_key = el.find("IncludePublicKey")
    if child_include_public_key is not None:
        out["include_public_key"] = (
            child_include_public_key.text or ""
        ).lower() == "true"
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    return out
