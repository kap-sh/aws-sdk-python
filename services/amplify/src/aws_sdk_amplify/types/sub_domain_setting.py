"""Generated from Smithy shape ``com.amazonaws.amplify#SubDomainSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.branch_name
    import aws_sdk_amplify.types.domain_prefix


class SubDomainSetting(TypedDict, closed=True):
    prefix: "aws_sdk_amplify.types.domain_prefix.DomainPrefix"
    """<p> The prefix setting for the subdomain. </p>"""
    branch_name: "aws_sdk_amplify.types.branch_name.BranchName"
    """<p> The branch name setting for the subdomain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubDomainSetting) -> dict:
    out: dict = {}
    out["prefix"] = value["prefix"]
    out["branchName"] = value["branch_name"]
    return out


def deserialize_json(data: dict) -> SubDomainSetting:
    out: SubDomainSetting = {}  # type: ignore[typeddict-item]
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    else:
        raise DeserializationError("SubDomainSetting.prefix required")
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    else:
        raise DeserializationError("SubDomainSetting.branch_name required")
    return out
