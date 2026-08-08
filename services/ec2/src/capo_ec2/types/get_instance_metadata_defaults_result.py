"""Generated from Smithy shape ``com.amazonaws.ec2#GetInstanceMetadataDefaultsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_metadata_defaults_response


class GetInstanceMetadataDefaultsResult(TypedDict, closed=True):
    account_level: NotRequired[
        "capo_ec2.types.instance_metadata_defaults_response.InstanceMetadataDefaultsResponse"
    ]
    """<p>The account-level default IMDS settings.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetInstanceMetadataDefaultsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "account_level" in value:
        import capo_ec2.types.instance_metadata_defaults_response

        capo_ec2.types.instance_metadata_defaults_response.serialize_ec2_query(
            value["account_level"], pairs, f"{key_prefix}AccountLevel"
        )


def deserialize_ec2_query(el: Element) -> GetInstanceMetadataDefaultsResult:
    out: GetInstanceMetadataDefaultsResult = {}  # type: ignore[typeddict-item]
    child_account_level = el.find("accountLevel")
    if child_account_level is not None:
        import capo_ec2.types.instance_metadata_defaults_response

        out["account_level"] = (
            capo_ec2.types.instance_metadata_defaults_response.deserialize_ec2_query(
                child_account_level
            )
        )
    return out
