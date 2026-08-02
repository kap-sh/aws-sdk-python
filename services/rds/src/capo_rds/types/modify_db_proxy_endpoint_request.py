"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBProxyEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_proxy_endpoint_name
    import capo_rds.types.string_list


class ModifyDBProxyEndpointRequest(TypedDict, closed=True):
    db_proxy_endpoint_name: NotRequired[
        "capo_rds.types.db_proxy_endpoint_name.DBProxyEndpointName"
    ]
    """<p>The name of the DB proxy sociated with the DB proxy endpoint that you want to modify.</p>"""
    new_db_proxy_endpoint_name: NotRequired[
        "capo_rds.types.db_proxy_endpoint_name.DBProxyEndpointName"
    ]
    """<p>The new identifier for the <code>DBProxyEndpoint</code>. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.</p>"""
    vpc_security_group_ids: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>The VPC security group IDs for the DB proxy endpoint. When the DB proxy endpoint uses a different VPC than the original proxy, you also specify a different set of security group IDs than for the original proxy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBProxyEndpointRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_proxy_endpoint_name" in value:
        pairs.append(
            (f"{key_prefix}DBProxyEndpointName", str(value["db_proxy_endpoint_name"]))
        )
    if "new_db_proxy_endpoint_name" in value:
        pairs.append(
            (
                f"{key_prefix}NewDBProxyEndpointName",
                str(value["new_db_proxy_endpoint_name"]),
            )
        )
    if "vpc_security_group_ids" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{key_prefix}VpcSecurityGroupIds"
        )


def deserialize_query(el: Element) -> ModifyDBProxyEndpointRequest:
    out: ModifyDBProxyEndpointRequest = {}  # type: ignore[typeddict-item]
    child_db_proxy_endpoint_name = el.find("DBProxyEndpointName")
    if child_db_proxy_endpoint_name is not None:
        out["db_proxy_endpoint_name"] = str(child_db_proxy_endpoint_name.text or "")
    child_new_db_proxy_endpoint_name = el.find("NewDBProxyEndpointName")
    if child_new_db_proxy_endpoint_name is not None:
        out["new_db_proxy_endpoint_name"] = str(
            child_new_db_proxy_endpoint_name.text or ""
        )
    child_vpc_security_group_ids = el.find("VpcSecurityGroupIds")
    if child_vpc_security_group_ids is not None:
        import capo_rds.types.string_list

        out["vpc_security_group_ids"] = capo_rds.types.string_list.deserialize_query(
            child_vpc_security_group_ids
        )
    return out
