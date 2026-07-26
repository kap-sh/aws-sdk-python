"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetTargetDomainsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.target_domain_id_list
    import capo_securityagent.types.target_domain_list


class BatchGetTargetDomainsOutput(TypedDict, closed=True):
    target_domains: NotRequired[
        "capo_securityagent.types.target_domain_list.TargetDomainList"
    ]
    """<p>The list of target domains that were found.</p>"""
    not_found: NotRequired[
        "capo_securityagent.types.target_domain_id_list.TargetDomainIdList"
    ]
    """<p>The list of target domain identifiers that were not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTargetDomainsOutput) -> dict:
    out: dict = {}
    if "target_domains" in value:
        import capo_securityagent.types.target_domain_list

        out["targetDomains"] = (
            capo_securityagent.types.target_domain_list.serialize_json(
                value["target_domains"]
            )
        )
    if "not_found" in value:
        import capo_securityagent.types.target_domain_id_list

        out["notFound"] = capo_securityagent.types.target_domain_id_list.serialize_json(
            value["not_found"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetTargetDomainsOutput:
    out: BatchGetTargetDomainsOutput = {}  # type: ignore[typeddict-item]
    if "targetDomains" in data:
        import capo_securityagent.types.target_domain_list

        out["target_domains"] = (
            capo_securityagent.types.target_domain_list.deserialize_json(
                data["targetDomains"]
            )
        )
    if "notFound" in data:
        import capo_securityagent.types.target_domain_id_list

        out["not_found"] = (
            capo_securityagent.types.target_domain_id_list.deserialize_json(
                data["notFound"]
            )
        )
    return out
