"""Generated from Smithy shape ``com.amazonaws.ec2#GetInstanceMetadataDefaultsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_metadata_defaults_response


class GetInstanceMetadataDefaultsResult(TypedDict):
    account_level: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_defaults_response.InstanceMetadataDefaultsResponse"
    ]
    """<p>The account-level default IMDS settings.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetInstanceMetadataDefaultsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "account_level" in value:
        import aws_sdk_ec2.types.instance_metadata_defaults_response

        aws_sdk_ec2.types.instance_metadata_defaults_response.serialize_ec2_query(
            value["account_level"], pairs, f"{prefix}.AccountLevel"
        )


def deserialize_ec2_query(el: Element) -> GetInstanceMetadataDefaultsResult:
    out: GetInstanceMetadataDefaultsResult = {}  # type: ignore[typeddict-item]
    child_account_level = el.find("AccountLevel")
    if child_account_level is not None:
        import aws_sdk_ec2.types.instance_metadata_defaults_response

        out["account_level"] = (
            aws_sdk_ec2.types.instance_metadata_defaults_response.deserialize_ec2_query(
                child_account_level
            )
        )
    return out
