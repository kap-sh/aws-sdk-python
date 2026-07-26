"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListVolumeInitiatorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.initiators


class ListVolumeInitiatorsOutput(TypedDict, closed=True):
    initiators: NotRequired["capo_storage_gateway.types.initiators.Initiators"]
    """<p>The host names and port numbers of all iSCSI initiators that are connected to the gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListVolumeInitiatorsOutput) -> dict:
    out: dict = {}
    if "initiators" in value:
        import capo_storage_gateway.types.initiators

        out["Initiators"] = (
            capo_storage_gateway.types.initiators.serialize_aws_json_1_1(
                value["initiators"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListVolumeInitiatorsOutput:
    out: ListVolumeInitiatorsOutput = {}  # type: ignore[typeddict-item]
    if "Initiators" in data:
        import capo_storage_gateway.types.initiators

        out["initiators"] = (
            capo_storage_gateway.types.initiators.deserialize_aws_json_1_1(
                data["Initiators"]
            )
        )
    return out
