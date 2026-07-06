"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ResoldUnifiedOperations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.account_id
    import aws_sdk_partnercentral_channel.types.coverage


class ResoldUnifiedOperations(TypedDict, closed=True):
    coverage: "aws_sdk_partnercentral_channel.types.coverage.Coverage"
    """<p>The coverage level for resold unified operations support.</p>"""
    tam_location: "str"
    """<p>The location of the Technical Account Manager (TAM).</p>"""
    charge_account_id: NotRequired[
        "aws_sdk_partnercentral_channel.types.account_id.AccountId"
    ]
    """<p>The AWS account ID to charge for the support plan.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResoldUnifiedOperations) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_channel.types.coverage

    out["coverage"] = (
        aws_sdk_partnercentral_channel.types.coverage.serialize_aws_json_1_0(
            value["coverage"]
        )
    )
    out["tamLocation"] = value["tam_location"]
    if "charge_account_id" in value:
        out["chargeAccountId"] = value["charge_account_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResoldUnifiedOperations:
    out: ResoldUnifiedOperations = {}  # type: ignore[typeddict-item]
    if "coverage" in data:
        import aws_sdk_partnercentral_channel.types.coverage

        out["coverage"] = (
            aws_sdk_partnercentral_channel.types.coverage.deserialize_aws_json_1_0(
                data["coverage"]
            )
        )
    else:
        raise DeserializationError("ResoldUnifiedOperations.coverage required")
    if "tamLocation" in data:
        out["tam_location"] = data["tamLocation"]
    else:
        raise DeserializationError("ResoldUnifiedOperations.tam_location required")
    if "chargeAccountId" in data:
        out["charge_account_id"] = data["chargeAccountId"]
    return out
