"""Generated from Smithy shape ``com.amazonaws.s3control#ListStorageLensConfigurationsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.continuation_token
    import aws_sdk_s3_control.types.storage_lens_configuration_list


class ListStorageLensConfigurationsResult(TypedDict):
    next_token: NotRequired[
        "aws_sdk_s3_control.types.continuation_token.ContinuationToken"
    ]
    """<p>If the request produced more than the maximum number of S3 Storage Lens configuration results, you can pass this value into a subsequent request to retrieve the next page of results.</p>"""
    storage_lens_configuration_list: NotRequired[
        "aws_sdk_s3_control.types.storage_lens_configuration_list.StorageLensConfigurationList"
    ]
    """<p>A list of S3 Storage Lens configurations.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListStorageLensConfigurationsResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])
    if "storage_lens_configuration_list" in value:
        import aws_sdk_s3_control.types.storage_lens_configuration_list

        aws_sdk_s3_control.types.storage_lens_configuration_list.serialize_xml_flat(
            value["storage_lens_configuration_list"], el, "StorageLensConfiguration"
        )


def deserialize_xml(el: Element) -> ListStorageLensConfigurationsResult:
    out: ListStorageLensConfigurationsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("StorageLensConfiguration") is not None:
        import aws_sdk_s3_control.types.storage_lens_configuration_list

        out["storage_lens_configuration_list"] = (
            aws_sdk_s3_control.types.storage_lens_configuration_list.deserialize_xml_flat(
                el, "StorageLensConfiguration"
            )
        )
    return out
