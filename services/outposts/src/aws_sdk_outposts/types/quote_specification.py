"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.quote_specification_type
    import aws_sdk_outposts.types.rack_specification_details
    import aws_sdk_outposts.types.server_specification_details


class QuoteSpecification(TypedDict):
    quote_specification_type: NotRequired[
        "aws_sdk_outposts.types.quote_specification_type.QuoteSpecificationType"
    ]
    """<p>The type of specification. Valid values are <code>NEW_RACK</code>, <code>UPDATED_RACK</code>, <code>EXISTING_RACK</code>, and <code>SERVER</code>.</p>"""
    existing_rack_specification_details: NotRequired[
        "aws_sdk_outposts.types.rack_specification_details.RackSpecificationDetails"
    ]
    """<p>The existing rack specification details, if the specification type is <code>UPDATED_RACK</code> or <code>EXISTING_RACK</code>.</p>"""
    final_rack_specification_details: NotRequired[
        "aws_sdk_outposts.types.rack_specification_details.RackSpecificationDetails"
    ]
    """<p>The final rack specification details after the quote is fulfilled.</p>"""
    server_specification_details: NotRequired[
        "aws_sdk_outposts.types.server_specification_details.ServerSpecificationDetails"
    ]
    """<p>The server specification details, if the specification type is <code>SERVER</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuoteSpecification) -> dict:
    out: dict = {}
    if "quote_specification_type" in value:
        import aws_sdk_outposts.types.quote_specification_type

        out["QuoteSpecificationType"] = (
            aws_sdk_outposts.types.quote_specification_type.serialize_json(
                value["quote_specification_type"]
            )
        )
    if "existing_rack_specification_details" in value:
        import aws_sdk_outposts.types.rack_specification_details

        out["ExistingRackSpecificationDetails"] = (
            aws_sdk_outposts.types.rack_specification_details.serialize_json(
                value["existing_rack_specification_details"]
            )
        )
    if "final_rack_specification_details" in value:
        import aws_sdk_outposts.types.rack_specification_details

        out["FinalRackSpecificationDetails"] = (
            aws_sdk_outposts.types.rack_specification_details.serialize_json(
                value["final_rack_specification_details"]
            )
        )
    if "server_specification_details" in value:
        import aws_sdk_outposts.types.server_specification_details

        out["ServerSpecificationDetails"] = (
            aws_sdk_outposts.types.server_specification_details.serialize_json(
                value["server_specification_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> QuoteSpecification:
    out: QuoteSpecification = {}  # type: ignore[typeddict-item]
    if "QuoteSpecificationType" in data:
        import aws_sdk_outposts.types.quote_specification_type

        out["quote_specification_type"] = (
            aws_sdk_outposts.types.quote_specification_type.deserialize_json(
                data["QuoteSpecificationType"]
            )
        )
    if "ExistingRackSpecificationDetails" in data:
        import aws_sdk_outposts.types.rack_specification_details

        out["existing_rack_specification_details"] = (
            aws_sdk_outposts.types.rack_specification_details.deserialize_json(
                data["ExistingRackSpecificationDetails"]
            )
        )
    if "FinalRackSpecificationDetails" in data:
        import aws_sdk_outposts.types.rack_specification_details

        out["final_rack_specification_details"] = (
            aws_sdk_outposts.types.rack_specification_details.deserialize_json(
                data["FinalRackSpecificationDetails"]
            )
        )
    if "ServerSpecificationDetails" in data:
        import aws_sdk_outposts.types.server_specification_details

        out["server_specification_details"] = (
            aws_sdk_outposts.types.server_specification_details.deserialize_json(
                data["ServerSpecificationDetails"]
            )
        )
    return out
