"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeAccountConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.account_configuration


class DescribeAccountConfigurationResponse(TypedDict, closed=True):
    account_configuration: NotRequired[
        "aws_sdk_medialive.types.account_configuration.AccountConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccountConfigurationResponse) -> dict:
    out: dict = {}
    if "account_configuration" in value:
        import aws_sdk_medialive.types.account_configuration

        out["accountConfiguration"] = (
            aws_sdk_medialive.types.account_configuration.serialize_json(
                value["account_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAccountConfigurationResponse:
    out: DescribeAccountConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "accountConfiguration" in data:
        import aws_sdk_medialive.types.account_configuration

        out["account_configuration"] = (
            aws_sdk_medialive.types.account_configuration.deserialize_json(
                data["accountConfiguration"]
            )
        )
    return out
