"""Generated from Smithy shape ``com.amazonaws.evs#ApplianceFqdn``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_evs.errors import DeserializationError
from aws_sdk_evs._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ApplianceFqdn: TypeAlias = str