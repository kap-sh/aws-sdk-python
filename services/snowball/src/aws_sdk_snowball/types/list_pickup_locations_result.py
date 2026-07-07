"""Generated from Smithy shape ``com.amazonaws.snowball#ListPickupLocationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snowball.types.address_list
    import aws_sdk_snowball.types.string


class ListPickupLocationsResult(TypedDict, closed=True):
    addresses: NotRequired["aws_sdk_snowball.types.address_list.AddressList"]
    """<p>Information about the address of pickup locations.</p>"""
    next_token: NotRequired["aws_sdk_snowball.types.string.String"]
    r"""<p>HTTP requests are stateless. To identify what object comes \"next\" in the list of <code>ListPickupLocationsResult</code> objects, you have the option of specifying <code>NextToken</code> as the starting point for your returned list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPickupLocationsResult) -> dict:
    out: dict = {}
    if "addresses" in value:
        import aws_sdk_snowball.types.address_list

        out["Addresses"] = aws_sdk_snowball.types.address_list.serialize_aws_json_1_1(
            value["addresses"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPickupLocationsResult:
    out: ListPickupLocationsResult = {}  # type: ignore[typeddict-item]
    if "Addresses" in data:
        import aws_sdk_snowball.types.address_list

        out["addresses"] = aws_sdk_snowball.types.address_list.deserialize_aws_json_1_1(
            data["Addresses"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
