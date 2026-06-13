"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DatasetVersion``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p> Dataset version identifier. Accepts \"DRAFT\" or a non-negative integer string representing a published version number. </p>"""
DatasetVersion: TypeAlias = str