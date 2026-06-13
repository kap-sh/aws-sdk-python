"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetTargetDomainsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.target_domain_id_list


class BatchGetTargetDomainsInput(TypedDict):
    target_domain_ids: (
        "aws_sdk_securityagent.types.target_domain_id_list.TargetDomainIdList"
    )
    """<p>The list of target domain identifiers to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTargetDomainsInput) -> dict:
    out: dict = {}
    import aws_sdk_securityagent.types.target_domain_id_list

    out["targetDomainIds"] = (
        aws_sdk_securityagent.types.target_domain_id_list.serialize_json(
            value["target_domain_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetTargetDomainsInput:
    out: BatchGetTargetDomainsInput = {}  # type: ignore[typeddict-item]
    if "targetDomainIds" in data:
        import aws_sdk_securityagent.types.target_domain_id_list

        out["target_domain_ids"] = (
            aws_sdk_securityagent.types.target_domain_id_list.deserialize_json(
                data["targetDomainIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetTargetDomainsInput.target_domain_ids required"
        )
    return out
